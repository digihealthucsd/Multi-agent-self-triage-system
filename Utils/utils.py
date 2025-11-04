import os
import json
import ast
import re

from langchain_openai import ChatOpenAI
import vertexai
from langchain_google_vertexai import ChatVertexAI
from langchain_anthropic import ChatAnthropic
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import AIMessage, HumanMessage
import google.generativeai as genai

import Flowcharts.flowcharts as flowcharts

def set_up_api_keys():
    openai_api_key = "your-openai-api-key"
    os.environ["OPENAI_API_KEY"] = openai_api_key
    gemini_api_key = "your-gemini-api-key"
    genai.configure(api_key=gemini_api_key)
    anthropic_api_key = "your-anthropic-api-key"
    os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key
    deepseek_api_key = "your-deepseek-api-key"
    os.environ["DEEPSEEK_API_KEY"] = deepseek_api_key

<<<<<<< HEAD
=======
def safe_json_parser(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # If JSON parsing fails, assume it's using single quotes and convert
        if 'np.float32(' in text:
            text = re.sub(r'np\.float32\(([^)]+)\)', r'\1', text)
        return ast.literal_eval(text)

>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
def platform_selection(platform, temp, model):
    """Select and initialize the appropriate LLM based on the platform."""
    
    if platform == "OPENAI":
        llm = ChatOpenAI(temperature=temp, model=model)
    elif platform == "GOOGLE":
<<<<<<< HEAD
        vertexai.init(project="your-project-id", location="your-location")
=======
        vertexai.init(project="your-project-id", location="your-project-location")
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
        llm = ChatVertexAI(temperature=temp, model=model)
    elif platform == "ANTHROPIC":
        llm = ChatAnthropic(temperature=temp, max_tokens=2048, model=model)
    elif platform == "DEEPSEEK":
        llm = ChatDeepSeek(temperature=temp, model=model)
    else:
        raise Exception("The system only supports three platforms: OpenAI, Google Vertex AI, Anthropic and DeepSeek.")
    
    return llm

<<<<<<< HEAD
def safe_json_parser(text):
    try:
        # if valid JSON
        return json.loads(text)
    except json.JSONDecodeError:
        # If JSON parsing fails, assume it's using single quotes and convert it
        if 'np.float32(' in text:
            text = re.sub(r'np\.float32\(([^)]+)\)', r'\1', text)
        return ast.literal_eval(text)

=======
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
def parse_rag_output(answer):
    """Parse the RAG output to extract the flowchart name or handle special cases."""
    
    answer_lower = re.sub(r'[\W_]+', '', answer.lower())
    flowchart_name = re.search(r'[A-Za-z ]+Flowchart', answer)
    if "noflowchartavailable" in answer_lower:
        return "no flowchart available"
    elif flowchart_name:
        return flowchart_name.group(0)
    else:
        return f"Not a valid RAG output: {answer}"
    
def flowchart_categories():
<<<<<<< HEAD
    """Categorize flowcharts into 10 medical specialties."""
=======
    """Define categories of flowcharts."""
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918

    general_medicine = ["Feeling Generally Ill Flowchart", "Unexplained Weight Loss Flowchart", "Overweight Flowchart", "Fever Flowchart", "Fever In Young Children Flowchart", "Fever In Children Flowchart", "Excessive Sweating Flowchart", "Slow Weight Gain In Young Children Flowchart"]
    neurology = ["Feeling Faint And Fainting Flowchart", "Dizziness Flowchart", "Headache Flowchart", "Numbness Or Tingling Flowchart", "Twitching And Trembling Flowchart", "Pain In The Face Flowchart", "Confusion Flowchart", "Confusion In Older People Flowchart", "Impaired Memory Flowchart", "Difficulty Speaking Flowchart"]
    mental_behavioral_health = ["Disturbing Thoughts Or Feelings Flowchart", "Unusual Behavior Flowchart", "Depression Flowchart", "Anxiety Flowchart", "Hallucinations Flowchart", "Nightmares Flowchart", "Difficulty Sleeping Flowchart", "Waking At Night In Children Flowchart", "Crying In Infants Flowchart"]
    dermatology = ["Hair Loss Flowchart", "General Skin Problems Flowchart", "Facial Skin Problems Flowchart", "Itchy Spots And Rashes Flowchart", "Itching Without A Rash Flowchart", "Rash With Fever Flowchart", "Raised Spots And Lumps Flowchart", "Abnormal Hair Growth In Women Flowchart", "Skin Problems In Young Children Flowchart", "Itching In Children Flowchart", "Swellings In Children Flowchart", "Swellings Under The Skin Flowchart"]
    eye_ent_oral_health = ["Painful Eye Flowchart", "Disturbed Or Impaired Vision Flowchart", "Earache Flowchart", "Noises In The Ear Flowchart", "Hearing Loss Flowchart", "Runny Nose Flowchart", "Sore Throat Flowchart", "Hoarseness Or Loss Of Voice Flowchart", "Toothache Flowchart", "Difficulty Swallowing Flowchart", "Sore Mouth Or Tongue Flowchart", "Bad Breath Flowchart"]
    pulmonology_cardiology = ["Coughing Flowchart", "Coughing Up Blood Flowchart", "Wheezing Flowchart", "Difficulty Breathing Flowchart", "Palpitations Flowchart", "Coughing In Children Flowchart", "Chest Pain Flowchart"]
    urology = ["Abnormally Frequent Urination Flowchart", "Abnormal Looking Urine Flowchart", "Painful Urination Flowchart", "Lack Of Bladder Control Flowchart", "Lack Of Bladder Control In Older People Flowchart"]
    gastroenterology = ["Vomiting Flowchart", "Recurring Vomiting Flowchart", "Abdominal Pain Flowchart", "Recurring Abdominal Pain Flowchart", "Swollen Abdomen Flowchart", "Gas And Belching Flowchart", "Diarrhea Flowchart", "Constipation Flowchart", "Abnormal Looking Stools Flowchart", "Vomiting In Infants Flowchart", "Diarrhea In Infants Flowchart", "Abdominal Pain In Children Flowchart"]
    musculoskeletal_system = ["Backache Flowchart", "Cramp Flowchart", "Painful Or Stiff Neck Flowchart", "Painful Arm Or Hand Flowchart", "Painful Leg Flowchart", "Painful Knee Flowchart", "Painful Shoulder Flowchart", "Painful Ankles Flowchart", "Swollen Ankles Flowchart", "Foot Problems Flowchart", "Limping In Children Flowchart"]
    reproductive_health = ["Painful Or Enlarged Testicles Flowchart", "Painful Intercourse In Men Flowchart", "Infertility In Men Flowchart", "Infertility In Women Flowchart", "Absent Periods Flowchart", "Heavy Periods Flowchart", "Painful Periods Flowchart", "Pelvic Pain In Women Flowchart", "Irregular Vaginal Bleeding Flowchart", "Abnormal Vaginal Discharge Flowchart", "Vaginal Irritation Flowchart", "Painful Intercourse In Women Flowchart", "Pain Or Lumps In The Breast Flowchart", "Breast Problems In New Mothers Flowchart"]

    flowchart_category_dict = {"General_Medicine": general_medicine, "Neurology": neurology, "Mental_and_Behavioral_Health": mental_behavioral_health, "Dermatology": dermatology, "Eye_Ear_Nose_Throat_and_Oral_Health": eye_ent_oral_health, "Pulmonology_and_Cardiology": pulmonology_cardiology, "Urology": urology, "Gastroenterology": gastroenterology, "Musculoskeletal_System": musculoskeletal_system, "Reproductive_Health": reproductive_health}

    return flowchart_category_dict

def get_flowchart_list():
    """Get a list of all flowcharts from all categories."""
    
    categories = flowchart_categories()
    flowchart_list = []
    for category in categories.values():
        flowchart_list.extend(category)
        
    return flowchart_list

def get_flowchart(answer):
<<<<<<< HEAD
    """Get the flowchart from the flowchart databse based on the RAG output answer."""
=======
    """Retrieve the flowchart and graph based on the RAG output answer."""
>>>>>>> e945b45bb8c81334b3db2069277cab1f8f062918
    
    if "no flowchart available" in answer:
        return "no authorization to answer"
    elif "Not a valid RAG output" in answer:
        return answer
    
    answer = answer.strip().replace(" ", "_")
    func_obj = getattr(flowcharts, answer, None)

    if func_obj is None:
        return f"{answer} not found"
    flowchart, graph = func_obj()
    
    return flowchart, graph

def nested_flowchart(flowchart):
    """Handle special cases of nested flowcharts."""
    
    remap_dict = {"Pelvic Pain In Women Flowchart": "Abdominal Pain Flowchart",
                  "Confusion In Older People Flowchart": "Confusion Flowchart", 
                  "Lack Of Bladder Control In Older People Flowchart": "Lack Of Bladder Control Flowchart"}
    
    return remap_dict[flowchart]

def get_next_step(graph, current_step, answer):
    """Get the next node in the flowchart graph based on the current step and answer."""
    
    for _, next_node, edge_data in graph.out_edges(current_step, data=True):
        if edge_data.get("condition") == answer:
            return next_node

    return None

def format_conversation_history(conversation):
    """Format the conversation history to meet langchain requirements."""
    
    history_langchain_format = []
    for text in conversation:
        if "Patient: " in text:
            patient = text.split("Patient: ")[1]
            history_langchain_format.append(HumanMessage(content=patient))
        elif "TriageMD: " in text: 
            triagemd = text.split("TriageMD: ")[1]
            history_langchain_format.append(AIMessage(content=triagemd))
        else:
            raise ValueError("Incorrect Format in Conversation")
        
    return history_langchain_format