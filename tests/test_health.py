"""API tests that do not call the language model."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_requires_message():
    response = client.post("/chat", json={})
    assert response.status_code == 422
