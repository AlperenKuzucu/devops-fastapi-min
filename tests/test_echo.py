from fastapi.testclient import TestClient
from app.main import app

def test_echo_roundtrip():
    client = TestClient(app)
    payload = {"a": 1, "b": {"c": [1, 2, 3]}, "ok": True}
    r = client.post("/echo", json=payload)
    assert r.status_code == 200
    assert r.json() == payload
