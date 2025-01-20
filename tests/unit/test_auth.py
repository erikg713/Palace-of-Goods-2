import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register(client):
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 201

def test_register_duplicate_username(client):
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'testuser2@example.com',
        'password': 'password123'
    })
    assert response.status_code == 400

def test_register_duplicate_email(client):
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    response = client.post('/api/auth/register', json={
        'username': 'testuser2',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 400

def test_login(client):
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_invalid_credentials(client):
    response = client.post('/api/auth/login', json={
        'username': 'invaliduser',
        'password': 'invalidpassword'
    })
    assert response.status_code == 401
