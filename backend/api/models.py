from pydantic import BaseModel, Field
from typing import List, Optional

# Matches React PatientInfo interface
class PatientInfo(BaseModel):
    name: str
    sex: str
    age: str
    isForSomeoneElse: bool

# Request models
class FlowchartRetrievalRequest(BaseModel):
    patient_info: PatientInfo
    opening_message: str

class ChatRequest(BaseModel):
    message: str
    patient_info: PatientInfo
    conversation: List[str]  # Format: ["Patient: ...", "TriageMD: ..."]
    current_node: str
    current_path: List[str]
    flowchart_name: str

# Logical flowchart models (structure only, no positioning)
class FlowNode(BaseModel):
    id: str
    label: str
    type: str  # 'start', 'question', 'decision', 'action', 'end'

class FlowEdge(BaseModel):
    from_: str = Field(alias="from")  # 'from' is Python keyword
    to: str
    label: Optional[str] = None
    
    class Config:
        populate_by_name = True

class FlowchartData(BaseModel):
    id: str
    name: str
    description: str
    nodes: List[FlowNode]
    edges: List[FlowEdge]

# Response models
class FlowchartRetrievalResponse(BaseModel):
    flowchart: FlowchartData
    similar_flowcharts: List[dict]
    retrieved: bool

class ChatResponse(BaseModel):
    response: str
    next_node: str
    current_path: List[str]
    prompt_type: int
    is_terminal: bool  # True if reached end/info node

