def ranking_agent(products, reviews, constraints):

    review_map = {r["product_id"]: r for r in reviews}

    ranked = []

    for p in products:
        sentiment = review_map.get(p["id"], {}).get("sentiment_score", 0.5)

        score = (
            0.4 * (1 - p.get("score", 0)) +
            0.3 * (p["rating"] / 5) +
            0.3 * sentiment
        )

        ranked.append({
            "id": p["id"],
            "title": p["title"],
            "price": p["price"],
            "rating": p["rating"],
            "final_score": score,
            "analysis": review_map.get(p["id"], {}).get("analysis", "")
        })

    return sorted(ranked, key=lambda x: x["final_score"], reverse=True)