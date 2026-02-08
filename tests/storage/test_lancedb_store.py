from src.storage.schema import Symbol
from src.storage.lancedb_store import store_symbols, vector_search
from src.utils.embedding.embedder import embed_texts

SYMBOLS_TABLE = "symbols"

def test_store_and_search():
    symbols = [
        Symbol(
            name="add",
            code="def add(a, b): return a + b",
            file="math_utils.py",
            language="python"
        )
    ]

    store_symbols(symbols)

    query_vec = embed_texts(["addition"])[0]
    results = vector_search(query_vec, SYMBOLS_TABLE, k=1)

    assert len(results) == 1
    assert "add" in results[0]["code"]
