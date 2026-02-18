# Code Search RAG

A **code-aware RAG system** that answers design and implementation questions by retrieving the **most relevant source files** from a repository and querying an LLM (via **Ollama**).

Instead of returning raw chunks, results are **deduplicated and ranked at the file level**, even when files are split into many chunks.

---

## What It Does

* 🔍 **Hybrid retrieval**

  * Semantic embeddings
  * BM25 lexical search
* 🧩 **Code-aware chunking**

  * Tree-sitter based
  * Language aware
* 🤖 **LLM answering**

  * Uses Ollama models
* 🚀 **FastAPI API**

---

## Architecture (High Level)

<img width="1381" height="773" alt="image" src="https://github.com/user-attachments/assets/1017c48a-3ccb-4b1e-81d5-cd460b408319" />


---

## Project Structure

```
src/
├── api/                  # FastAPI endpoints
│   └── api.py
│
├── retrieval/
│   ├── semantic/
│   │   ├── chunker/
│   │   │   └── tree_sitter_chunker.py
│   ├── bm25/
│   └── retriever.py
│
├── utils/
│   └── embedding/
│
├── llm/
│   ├── prompt.py
│   └── ollama_client.py
│
├── storage/
└── db/
```

Tests:

```
tests/
├── chunker/
├── retrieval/
└── api/
```

---

## Installation

```bash
git clone <repo-url>
cd code-search-rag
pip install -e .
```

**Important:** this repo uses a `src/` layout.
`pyproject.toml` must include:

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

---

## Ollama Setup

```bash
ollama serve
ollama pull llama3
```

Configure the model in `llm/ollama_client.py`.

---

## Run the API

```bash
uvicorn api.api:app --reload
```

If the port is busy:

```bash
uvicorn api.api:app --port 8000
```

---

## API

### Endpoint

```
POST /ask-about-design
```

### Request

```json
{
  "query": "How is semantic retrieval implemented?"
}
```



```
POST /file-locator
```

### Request

```json
{
  "query": "Where is semantic retrieval implemented?"
}
```

---

## Chunking & Ranking

* Files are split into **multiple code chunks**
* Each chunk has a unique ID
* Retrieval happens at the **chunk level**
* Results are **collapsed to file level**
* The highest-scoring chunk defines the file score

This prevents noisy duplicate results while preserving relevance.

---

## Testing

```bash
pytest
```

Tests use **absolute imports**:

```python
from retrieval.semantic.chunker.tree_sitter_chunker import TreeSitterChunker
```

Ensure all packages contain `__init__.py`.

---

## Common Issues

### `ModuleNotFoundError`

* Install with `pip install -e .`
* Use `src/` layout
* Do not run tests from inside subdirectories

---

## Roadmap

* Language-specific chunkers (C++, Java, Python)
* Better file-level scoring strategies
* Cross-repo search
* UI for browsing ranked files
* Incremental indexing

---

## Design Goal

> **Answer the question and show exactly where the answer lives.**

This system prioritizes **file-level relevance, traceability, and trust** over opaque LLM responses.

