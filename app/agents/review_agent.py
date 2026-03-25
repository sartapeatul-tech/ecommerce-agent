from langsmith import traceable

@traceable(name="review_agent")

def review_agent(products, query):
    results = []

    for p in products[:5]:
        results.append({
            "product_id": p["id"],
            "analysis": "Good product with positive reviews.",
            "sentiment_score": 0.8
        })

    return results

    return results