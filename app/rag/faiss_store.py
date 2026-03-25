import faiss
import pickle

def load_faiss():
    index = faiss.read_index('vector_store/index.faiss')
    with open('vector_store/products.pkl', 'rb') as f:
        products = pickle.load(f)
    return index, products