from src.retrieval.semantic.semantic_search import semantic_search
from src.retrieval.search.bm25_search import bm25_search

def retrieve(query, k=5, mode="file", strategy="hybrid"):
    semantic_results = semantic_search(query, k)
    bm25_results = bm25_search(query, k)

    combined_results = semantic_results + bm25_results

    return combined_results[:k]

def locate_files(query: str, k = 5):
    semantic_results = semantic_search(query, k * 2)
    bm25_results = bm25_search(query, k)

    combined_results = semantic_results + bm25_results

    seen = set()

    for result in combined_results:
        f = result["file"]
        if f in seen:
            continue
        seen.add(f)

    return [file for file in seen]

