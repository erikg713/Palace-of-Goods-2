import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

def test_register(client):
    response = client.post('/auth/register', json={"username": "test", "password": "password"})
    assert response.status_code == 201

def test_login(client):
    client.post('/auth/register', json={"username": "test", "password": "password"})
    response = client.post('/auth/login', json={"username": "test", "password": "password"})
    assert response.status_code == 200
