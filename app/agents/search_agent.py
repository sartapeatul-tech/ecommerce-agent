from app.rag.embedder import embed_query
from app.rag.faiss_store import load_faiss
import numpy as np
import re

index, products = load_faiss()

def extract_constraints(query):
    constraints = {}
    match = re.search(r"under (\d+)", query)
    if match:
        constraints["max_price"] = float(match.group(1))
    return constraints

def search_agent(query, top_k=10):
    query_vec = embed_query(query)
    query_vec = np.array([query_vec]).astype("float32")

    distances, indices = index.search(query_vec, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        p = products[idx]
        p["score"] = float(distances[0][i])
        results.append(p)

    constraints = extract_constraints(query)
    return results, constraints