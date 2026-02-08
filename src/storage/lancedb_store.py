import lancedb
from src.utils.embedding.embedder import embed_texts, expected_embeddings_length
import pyarrow as pa

db = lancedb.connect("./db/code_rag")

schema = pa.schema([
    pa.field("vector", pa.list_(pa.float32(), 384)),
    pa.field("code", pa.utf8()),
    pa.field("file", pa.utf8()),
    pa.field("language", pa.utf8()),
    pa.field("name", pa.utf8())
])

def is_valid_code_chunk(code: str) -> bool:
    if not code:
        return False
    code = code.strip()
    if len(code) < 20:
        return False
    # avoid pure comments / noise
    if code.startswith(("#", "//", "/*")):
        return False
    return True

# Store code parsed as symbols into a table
def store_symbols(symbols, table_name = "symbols"):
    table = db.create_table(table_name, data=[], schema=schema, mode="overwrite")

    embeddings = embed_texts([s.code for s in symbols])
    expected_vector_length = expected_embeddings_length(embeddings)

    rows = []
    for s, e in zip(symbols, embeddings):
        if len(e) != expected_vector_length:
            continue
        if not is_valid_code_chunk(s.code):
            continue
        rows.append({
            "vector": e,
            "code": s.code,
            "file": s.file,
            "language": s.language,
            "name": s.name,
        })

    if len(rows) == 0:
        raise RuntimeError("All rows dropped after embedding validation")

    table.add(rows)

# Searches for k-closest vectors for a given vector
def vector_search(vector, table_name, k=10):
    return (
        db.open_table(table_name)
        .search(vector)
        .limit(k)
        .to_list()
    )
