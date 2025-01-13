import pytest
from app import create_app, db
from models.user import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_register(client):
    response = client.post('/api/auth/register', json={
        "username": "testuser",
        "password": "testpassword",
        "email": "test@example.com"
    })
    assert response.status_code == 201
    assert response.json['msg'] == "User registered successfully"