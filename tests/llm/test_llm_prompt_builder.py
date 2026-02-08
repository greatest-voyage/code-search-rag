from src.llm.prompt import build_prompt

def test_prompt_contains_context():
    query = "Explain design"
    contexts = [
        {"file": "a.py", "code": "def foo(): pass"}
    ]

    prompt = build_prompt(query, contexts)

    assert "Explain design" in prompt
    assert "a.py" in prompt
    assert "def foo" in prompt
