def test_get_products(test_client, init_database):
    response = test_client.get("/products/")
    assert response.status_code == 200
    products = response.get_json()
    assert len(products) > 0
    assert products[0]["name"] == "Test Product"

def test_create_product(test_client, init_database):
    # Use an admin user's token for authentication
    token_response = test_client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    token = token_response.get_json()["access_token"]

    response = test_client.post(
        "/products/",
        json={
            "name": "New Product",
            "description": "A new sample product",
            "price": 20.50
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    assert response.get_json()["message"] == "Product created successfully"
