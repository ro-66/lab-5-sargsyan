from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps Lab 5"}

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_existing_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Robert"

def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 200
    assert response.json() == {"error": "User not found"}
