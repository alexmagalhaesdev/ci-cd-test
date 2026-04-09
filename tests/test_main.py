from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_item() -> None:
    payload = {"name": "Keyboard", "quantity": 2}
    response = client.post("/items", json=payload)
    assert response.status_code == 200
    assert response.json() == payload

