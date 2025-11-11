"""
TriageMD FastAPI Backend
Wraps existing Python triage logic with REST API
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import re
from typing import List, Tuple, Optional
from dotenv import load_dotenv

# Add parent directories to path for imports
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
project_root = os.path.dirname(backend_dir)
sys.path.append(project_root)

# Load environment variables from project root .env file
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

import System.system_implementation as triagemd
import Utils.utils as utils
from api.models import (
    FlowchartRetrievalRequest, FlowchartRetrievalResponse,
    ChatRequest, ChatResponse
)
from api.converter import convert_to_visual_flowchart


def slugify_flowchart_name(name: str) -> str:
    """
    Convert flowchart name to slug (lowercase, hyphen separated).
    """
    cleaned = re.sub(r"[^\w\s-]", "", name).strip().lower()
    return re.sub(r"[\s_]+", "-", cleaned)


def parse_flowchart_metadata(content: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse a line from flowchart_descriptions.txt to extract the flowchart name and description.
    Expected format:
        AgeRange - Sex - Flowchart Name - Description
    """
    if not content:
        return None, None
    parts = [part.strip() for part in content.split(" - ") if part.strip()]
    if len(parts) < 3:
        return None, None
    name_candidates = [part for part in parts if part.endswith("Flowchart")]
    flowchart_name = name_candidates[0] if name_candidates else None
    description_index = parts.index(flowchart_name) + 1 if flowchart_name in parts else None
    description = None
    if description_index is not None and description_index < len(parts):
        description = " - ".join(parts[description_index:])
    return flowchart_name, description


def build_recommendation_list(primary_name: str, retrieved_candidates: List[dict], max_results: int = 3) -> List[Tuple[str, Optional[str]]]:
    """
    Combine the LLM-selected flowchart with the top FAISS candidates.
    Returns an ordered list of (name, description) tuples with unique names.
    """
    ordered: List[Tuple[str, Optional[str]]] = []

    def add_candidate(name: Optional[str], description: Optional[str]) -> None:
        if not name:
            return
        name = name.strip()
        if name not in [item[0] for item in ordered]:
            ordered.append((name, description))

    add_candidate(primary_name, None)

    for item in retrieved_candidates:
        name, description = parse_flowchart_metadata(item.get("content", ""))
        if not name:
            continue
        add_candidate(name, description)

    return ordered[:max_results]

# Initialize FastAPI app
app = FastAPI(
    title="TriageMD API",
    description="Medical triage chatbot API using AMA flowcharts",
    version="1.0.0"
)

# CORS - allow frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative port
        "https://*.github.io"     # GitHub Pages (production)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM once at startup
utils.set_up_api_keys()
llm = utils.platform_selection("OPENAI", 0.0, "gpt-4o-mini")
# Go up from backend/api/ to project root, then to Flowcharts
flowchart_description_file = os.path.join(
    project_root,
    "Flowcharts",
    "flowchart_descriptions.txt"
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "TriageMD API"}

@app.post("/api/retrieve-flowchart", response_model=FlowchartRetrievalResponse)
async def retrieve_flowchart(request: FlowchartRetrievalRequest):
    """
    Retrieve appropriate flowchart based on patient's opening message
    Uses existing RAG retrieval logic from system_implementation.py
    """
    try:
        # Format patient demographics
        demographics = f"Sex - {request.patient_info.sex}, Age - {request.patient_info.age}"
        first_message = f"Patient's demographics: {demographics}; Patient's concern: {request.opening_message}"
        
        # Use existing retrieval_agent (RAG with FAISS) to retrieve top candidates
        llm_choice_raw, retrieved_candidates = triagemd.retrieval_agent(
            flowchart_description_file,
            first_message,
            llm,
            k=10,
            retrieve=True
        )

        # Normalize LLM choice
        primary_choice = utils.parse_rag_output(llm_choice_raw).strip()
        if primary_choice == "no flowchart available":
            raise HTTPException(
                status_code=404,
                detail="No relevant flowchart available for this symptom description."
            )

        # Determine if primary choice is within top FAISS candidates
        faiss_names = [
            parse_flowchart_metadata(item.get("content", ""))[0]
            for item in retrieved_candidates
            if parse_flowchart_metadata(item.get("content", ""))[0]
        ]
        primary_in_faiss = primary_choice in faiss_names

        # If primary is in top 10 → return 3 recommendations total (primary + 2)
        # If primary not in top 10 → return 4 total (primary + 3)
        max_recommendations = 3 if primary_in_faiss else 4

        # Build ordered recommendation list: primary + two alternates
        recommendations = build_recommendation_list(
            primary_choice,
            retrieved_candidates,
            max_results=max_recommendations,
        )
        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail="Unable to determine relevant flowcharts."
            )

        primary_name = recommendations[0][0]
        
        # Handle nested flowcharts (3 special cases)
        special_cases = {
            "Pelvic Pain In Women Flowchart",
            "Confusion In Older People Flowchart",
            "Lack Of Bladder Control In Older People Flowchart"
        }
        if primary_name in special_cases:
            primary_name = utils.nested_flowchart(primary_name)
        
        # Get flowchart from database (utils.py)
        flowchart_result = utils.get_flowchart(primary_name)
        
        if isinstance(flowchart_result, tuple):
            flowchart_dict, graph = flowchart_result
            
            # Convert to visual format (NEW FUNCTION)
            visual_flowchart = convert_to_visual_flowchart(
                primary_name,
                flowchart_dict,
                graph
            )

            # Prepare alternate recommendations (metadata only)
            similar_flowcharts = []
            for name, description in recommendations[1:]:
                adjusted_name = utils.nested_flowchart(name) if name in special_cases else name
                similar_flowcharts.append({
                    "id": slugify_flowchart_name(adjusted_name),
                    "name": adjusted_name,
                    "description": description or ""
                })

            return FlowchartRetrievalResponse(
                flowchart=visual_flowchart,
                similar_flowcharts=similar_flowcharts,
                retrieved=True
            )
        else:
            raise HTTPException(
                status_code=404,
                detail=f"No relevant flowchart found: {flowchart_result}"
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Handle chat interaction and navigate flowchart
    Uses existing decision_agent and chat_agent logic
    """
    try:
        # Get flowchart for current session
        flowchart_result = utils.get_flowchart(request.flowchart_name)
        
        if not isinstance(flowchart_result, tuple):
            raise HTTPException(
                status_code=400,
                detail="No flowchart loaded for this session"
            )
        
        flowchart_dict, graph = flowchart_result
        
        # Use existing determine_next_step (decision agent + navigation)
        current_node, flowchart_dict, graph, current_path, prompt_type, num_of_off_topic, num_of_uncertain = \
            triagemd.determine_next_step(
                flowchart_dict,
                graph,
                request.conversation,
                request.current_node,
                request.current_path,
                llm,
                num_of_off_topic=0,  # Reset for each message
                num_of_uncertain=0
            )
        
        # Format conversation history for LangChain
        history_langchain = utils.format_conversation_history(request.conversation)
        
        # Check if too many uncertain/off-topic responses
        if num_of_uncertain > 3 or num_of_off_topic > 3:
            response_text = triagemd.chat_agent(
                request.message,
                triagemd.chat_agent_prompt_mapping()[1],
                "Sorry, I can't proceed due to lack of information. Please consult a healthcare professional.",
                llm,
                history_langchain
            )
            is_terminal = True
        else:
            # Use existing chat_agent to generate response
            response_text = triagemd.chat_agent(
                request.message,
                triagemd.chat_agent_prompt_mapping()[prompt_type],
                flowchart_dict[current_node],
                llm,
                history_langchain
            )
            # Check if reached terminal node (Info or Flowchart-switch nodes)
            is_terminal = current_node.startswith('I') or current_node.startswith('F')
        
        return ChatResponse(
            response=response_text,
            next_node=current_node,
            current_path=current_path,
            prompt_type=prompt_type,
            is_terminal=is_terminal
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with: uvicorn api.main:app --reload --port 8000

