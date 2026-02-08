from src.retrieval.semantic.semantic_search import semantic_search

def test_semantic_search_returns_results():
    results = semantic_search("add two numbers", k=3)
    assert isinstance(results, list)
