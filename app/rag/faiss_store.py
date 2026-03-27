import os
import faiss
import pickle

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
VECTOR_STORE_DIR = os.path.join(BASE_DIR, 'vector_store')
INDEX_PATH = os.path.join(VECTOR_STORE_DIR, 'index.faiss')
PRODUCTS_PATH = os.path.join(VECTOR_STORE_DIR, 'products.pkl')

os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

def load_faiss():
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError(
            f"FAISS index file not found: {INDEX_PATH}. Run build_index.py first."
        )
    if not os.path.exists(PRODUCTS_PATH):
        raise FileNotFoundError(
            f"Products file not found: {PRODUCTS_PATH}. Run build_index.py first."
        )

    index = faiss.read_index(INDEX_PATH)
    with open(PRODUCTS_PATH, 'rb') as f:
        products = pickle.load(f)
    return index, products