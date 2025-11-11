"""
Converts Python flowchart format (dict + NetworkX graph) to logical graph structure.
Frontend handles layout with React Flow + Dagre.
"""

import networkx as nx
from typing import Dict
from api.models import FlowNode, FlowEdge, FlowchartData

def determine_node_type(node_id: str) -> str:
    """
    Determine node type from ID prefix
    N = question, A = action, F = end, I = decision
    """
    prefix = node_id[0] if node_id else 'N'
    type_map = {
        'N': 'question',
        'A': 'action', 
        'F': 'end',
        'I': 'decision'
    }
    return type_map.get(prefix, 'question')

def convert_to_visual_flowchart(
    flowchart_name: str,
    flowchart_dict: Dict[str, str],
    graph: nx.DiGraph
) -> FlowchartData:
    """
    Convert Python flowchart to logical structure (no positioning).
    React Flow will handle layout on frontend.
    """
    
    nodes = []
    for node_data in graph.nodes(data=False):
        # NetworkX may return tuples, extract just the ID
        if isinstance(node_data, tuple):
            node_id = node_data[0]
        else:
            node_id = node_data
            
        label = flowchart_dict.get(node_id, "")
        node_type = determine_node_type(node_id)
        
        nodes.append(FlowNode(
            id=node_id,
            label=label,
            type=node_type
        ))
    
    # Extract edges with conditions
    edges = []
    for from_node, to_node, data in graph.edges(data=True):
        edges.append(FlowEdge(
            from_=from_node,
            to=to_node,
            label=data.get('condition')  # "Yes", "No", or None
        ))
    
    return FlowchartData(
        id=flowchart_name.lower().replace(' ', '-').replace('_', '-'),
        name=flowchart_name,
        description=f"Clinical assessment flowchart for {flowchart_name}",
        nodes=nodes,
        edges=edges
    )
