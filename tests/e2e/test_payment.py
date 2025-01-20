import pytest
import requests

def test_complete_payment():
    login_url = "http://localhost:5000/api/auth/login"
    payment_url = "http://localhost:5000/api/complete-payment"
    
    login_payload = {
        "username": "testuser",
        "password": "password123"
    }
    
    payment_payload = {
        "payment_id": "unique_payment_id",
        "total_amount": 100,
        "txid": "sample_txid"
    }
    
    with requests.Session() as session:
        # Log in
        login_response = session.post(login_url, json=login_payload)
        assert login_response.status_code == 200
        
        # Complete payment
        payment_response = session.post(payment_url, json=payment_payload)
        assert payment_response.status_code == 200
        assert payment_response.json().get("message") == "Payment completed"
