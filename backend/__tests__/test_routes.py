import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
    yield app.test_client()

def test_get_products(client):
    response = client.get("/api/products")
    assert response.status_code == 200
    assert response.json == {"products": [], "total": 0, "pages": 0, "current_page": 1}

def test_register_user(client):
    response = client.post("/api/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert "username" in response.json
