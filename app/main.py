import os
import sys
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "ecommerce-agent-v2"

sys.path.append(os.path.dirname(__file__))

from app.graph.build_graph import build_graph

def run(query: str):
    graph = build_graph()

    state = {
        "query": query,
        "products": [],
        "constraints": {},
        "filtered_products": [],
        "review_analysis": [],
        "ranked_products": [],
        "final_output": ""
    }

    result = graph.invoke(state)
    return result["final_output"]


if __name__ == "__main__":
    query = "wireless headphones under 100"
    output = run(query)
    print("\n\nResult:\n", output)

#somesh gawande