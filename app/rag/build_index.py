import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from app.rag.data_loader import load_products
from app.rag.embedder import embed_query
import faiss
import numpy as np
import pickle

products = load_products()

# Assume products have 'description' field
embeddings = []
for p in products:
    emb = embed_query(p['description'])
    embeddings.append(emb)

embeddings = np.array(embeddings).astype('float32')

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, 'vector_store/index.faiss')

# Save products
with open('vector_store/products.pkl', 'wb') as f:
    pickle.dump(products, f)

print("Index built and saved.")