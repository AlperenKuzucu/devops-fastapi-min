from fastapi.testclient import TestClient
from app.main import app
from app.config import get_settings

def test_version_fields(monkeypatch):
    # settings cache'ini temizle ki test env'lerini alsın
    get_settings.cache_clear()

    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("APP_COMMIT", "testcommit123")

    client = TestClient(app)
    r = client.get("/version")
    assert r.status_code == 200

    data = r.json()
    assert data["version"] == "0.1.0"
    assert data["env"] == "dev"
    assert data["commit"] == "testcommit123"
