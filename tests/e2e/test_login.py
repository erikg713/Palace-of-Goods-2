import pytest
import requests

def test_login_success():
    url = "http://localhost:5000/api/auth/login"
    payload = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json().get("message") == "Login successful"

def test_login_failure():
    url = "http://localhost:5000/api/auth/login"
    payload = {
        "username": "invaliduser",
        "password": "wrongpassword"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 401
    assert response.json().get("message") == "Invalid username or password"
