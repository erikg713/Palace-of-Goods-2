def test_end_to_end_product_creation(test_client):
    # Step 1: Register a new user
    test_client.post("/auth/register", json={
        "username": "integrationuser",
        "password": "integrationpassword"
    })

    # Step 2: Login and get token
    login_response = test_client.post("/auth/login", json={
        "username": "integrationuser",
        "password": "integrationpassword"
    })
    token = login_response.get_json()["access_token"]

    # Step 3: Create a product
    create_response = test_client.post(
        "/products/",
        json={
            "name": "Integration Product",
            "description": "A product for integration testing",
            "price": 30.00
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert create_response.status_code == 201
    assert create_response.get_json()["message"] == "Product created successfully"

    # Step 4: Fetch the product
    get_response = test_client.get("/products/")
    products = get_response.get_json()
    assert any(p["name"] == "Integration Product" for p in products)
