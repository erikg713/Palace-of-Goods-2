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
