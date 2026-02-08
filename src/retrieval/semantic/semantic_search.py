from src.utils.embedding.embedder import embed_texts
from src.storage.lancedb_store import vector_search

# Table which stores repo parsed as chunks
SYMBOLS_TABLE = "symbols"

def semantic_search(query: str, k: int):
    vector = embed_texts([query])[0]
    return vector_search(vector, SYMBOLS_TABLE, k)