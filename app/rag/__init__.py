"""RAG module for the ecommerce agent."""

from .data_loader import load_products
from .embedder import embed_query
from .faiss_store import load_faiss