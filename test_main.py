from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Ping API is running!"}

def test_ping_valid_ip():
    response = client.get("/ping/8.8.8.8")
    assert response.status_code == 200
    assert "status" in response.json()

def test_ping_invalid_ip():
    response = client.get("/ping/hello")
    assert response.status_code == 422
