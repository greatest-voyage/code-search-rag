from retrieval.semantic.chunker.tree_sitter_chunker import TreeSitterChunker
from storage.lancedb_store import store_symbols

REPO_TO_CHUNK = "/Users/mohit/Desktop/Code/PycharmProjects/ollama/"


def bootstrap():
    print("Bootstrapping LLM")
    chunker = TreeSitterChunker()
    symbols = chunker.chunk_repo(REPO_TO_CHUNK)
    store_symbols(symbols)

