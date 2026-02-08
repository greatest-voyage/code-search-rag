from fastapi.testclient import TestClient
from src.api.api import app

client = TestClient(app)

def test_api_endpoint():
    resp = client.post(
        "/ask-about-design",
        json={"query": "How does addition work?"}
    )

    assert resp.status_code == 200
    assert "answer" in resp.json()

