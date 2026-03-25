from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    query: str
    products: List[Dict[str, Any]]
    constraints: Dict[str, Any]
    filtered_products: List[Dict[str, Any]]
    review_analysis: List[Dict[str, Any]]
    ranked_products: List[Dict[str, Any]]
    final_output: str