from src.utils.embedding.embedder import embed_texts

def test_embedding_shape():
    vecs = embed_texts(["hello world"])

    assert isinstance(vecs, list)
    assert len(vecs) == 1
    assert isinstance(vecs[0], list)
    assert len(vecs[0]) > 100  # model-specific, keep loose
