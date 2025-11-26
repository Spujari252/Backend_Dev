import pytest
from fastapi.testclient import TestClient
from random import randint
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

def test_when_given_user_name_should_create_a_student_in_db(client):
    random = randint(1, 10000)
    user_name = f"user{random}"
    last_name = f"last{random}"
    create_response = client.post("/students/", json={"first_name": user_name, "last_name": last_name})
    assert create_response.status_code == 200
    student_id = create_response.json()["id"]
    assert student_id is not None