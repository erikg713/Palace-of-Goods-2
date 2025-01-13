import pytest
from app import create_app, db
from models.user import User
from models.item import Item

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_item(client):
    # Create a user
    user = User(username="testuser", password="testpassword")
    db.session.add(user)
    db.session.commit()

    # Log in to get token
    response = client.post('/api/auth/login', json={"username": "testuser", "password": "testpassword"})
    token = response.json['access_token']

    # Add an item
    response = client.post(
        '/api/items/',
        json={"name": "Test Item", "category": "Electronics", "price": 99.99},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    assert response.json['msg'] == "Item added successfully"