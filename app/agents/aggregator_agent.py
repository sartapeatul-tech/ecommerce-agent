
from langsmith import traceable

@traceable(name="aggregator_agent")
    
def aggregator_agent(products, query):

    top = products[:3]

    text = ""
    for p in top:
        text += f"{p['title']} | {p['price']} | {p['rating']}\n{p.get('analysis', '')}\n\n"

    return f"Based on your query '{query}', here are the top recommendations:\n{text}"