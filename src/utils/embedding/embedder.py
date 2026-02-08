from nomic import embed
from sentence_transformers import SentenceTransformer

MODEL_NO = "nomic-embed-text-v1.5"

model_STR = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    return model_STR.encode(texts, normalize_embeddings=True).tolist()

def embed_texts_no(texts: list[str]) -> list[list[float]]:
    out = embed.text(texts=texts, model=MODEL_NO)
    return out["embeddings"]

def expected_embeddings_length(embeddings):
    if not embeddings:
        raise ValueError("No embeddings returned")

    dims = set()
    for i, e in enumerate(embeddings):
        if not isinstance(e, list):
            raise TypeError(f"Embedding {i} is not a list")
        if len(e) == 0:
            raise ValueError(f"Embedding {i} is empty")
        dims.add(len(e))

    if len(dims) != 1:
        raise ValueError(f"Inconsistent embedding dimensions: {dims}")

    return dims.pop()
