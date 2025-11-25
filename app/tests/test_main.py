import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def client():    
    with TestClient(app) as c:
        yield c


def test_when_app_running_status_endpoint_should_return_ok(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "ok"