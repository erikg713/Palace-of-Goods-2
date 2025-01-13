import pytest
from app import create_app, db
from models.payment import Payment

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_payment(client):
    # Simulate creating a payment
    response = client.post('/api/payments/create', json={
        "amount": 10.0,
        "memo": "Test Payment"
    })
    assert response.status_code == 201
    assert "payment_id" in response.json

def test_complete_payment(client):
    # Simulate completing a payment
    payment_id = "test-payment-id"
    response = client.post('/api/payments/complete', json={"payment_id": payment_id})
    assert response.status_code == 200

def test_create_payment(client):
    # Simulate authenticated user
    user_id = 1  # Assume a user ID is available
    response = client.post('/api/payments/create', json={
        "amount": 10.0,
        "memo": "Test Payment"
    }, headers={"Authorization": f"Bearer {generate_token(user_id)}"})
    assert response.status_code == 201
    assert "payment_id" in response.json