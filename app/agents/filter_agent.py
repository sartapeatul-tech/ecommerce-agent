def filter_agent(products, query):
    filtered = []

    max_price = None
    if "under" in query:
        try:
            max_price = int(query.split("under")[1].strip().split()[0])
        except (IndexError, ValueError):
            max_price = None

    for p in products:
        if max_price and p["price"] > max_price:
            continue

        p["feature_score"] = 1 if "camera" in query.lower() else 0
        filtered.append(p)

    return filtered