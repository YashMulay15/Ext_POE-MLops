from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    r = client.get("/")
    assert r.status_code == 200


def test_add_endpoint():
    r = client.post("/add", json={"a": 10, "b": 15})
    assert r.status_code == 200
    assert r.json()["result"] == 25


def test_add_invalid_input():
    r = client.post("/add", json={"a": "abc", "b": 5})
    assert r.status_code == 422