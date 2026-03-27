import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from app.rag.data_loader import load_products
from app.rag.embedder import embed_query
import faiss
import numpy as np
import pickle

products = load_products()

# Ensure vector_store folder exists
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
vector_store_dir = os.path.join(base_dir, 'vector_store')
os.makedirs(vector_store_dir, exist_ok=True)

index_path = os.path.join(vector_store_dir, 'index.faiss')
products_path = os.path.join(vector_store_dir, 'products.pkl')

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
faiss.write_index(index, index_path)

# Save products
with open(products_path, 'wb') as f:
    pickle.dump(products, f)

print(f"Index built and saved to {index_path}")