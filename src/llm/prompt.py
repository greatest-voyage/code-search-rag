import requests

# Expects contexts = [{file: , code: }]
def build_prompt(query, contexts):
    ctx = "\n\n".join(
        f"File: {c['file']}\n{c['code'][:1000]}"
        for c in contexts
    )

    return f"""
You are a Principal Systems Architect. Use the provided code chunks to explain the data flow.

Question:
{query}

Context:
{ctx}

Answer:
"""

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3.1:8b"  # or codellama, deepseek-coder, etc.

def ask_llm(query: str, contexts) -> str:
    prompt = build_prompt(query, contexts)

    resp = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["response"]
