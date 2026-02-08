from src.retrieval.semantic.chunker.tree_sitter_chunker import TreeSitterChunker

def test_basic_chunker_extracts_files():
    chunker = TreeSitterChunker()
    symbols = chunker.chunk_repo("/Users/mohit/PycharmProjects/code-search-rag/tests/fixtures/sample_repo/")

    assert len(symbols) > 0
    assert symbols[0].code
    assert symbols[0].file.endswith(".py")
