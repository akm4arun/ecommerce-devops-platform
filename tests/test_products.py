from app.main import create_app


def test_get_products():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/products")

    assert response.status_code == 200

    products = response.get_json()

    assert len(products) == 3
    assert products[0]["name"] == "Laptop"


def test_get_product():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/products/1")

    assert response.status_code == 200

    product = response.get_json()

    assert product["id"] == 1
    assert product["name"] == "Laptop"
    assert product["price"] == 75000


def test_get_product_not_found():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/products/999")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "product not found"
    }


def test_create_product():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/products",
        json={
            "name": "Monitor",
            "price": 26990,
            "category": "Electronics",
        },
    )

    assert response.status_code == 201

    product = response.get_json()

    assert product["name"] == "Monitor"
    assert product["price"] == 26990
    assert product["category"] == "Electronics"


def test_create_product_missing_fields():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/products",
        json={
            "name": "Monitor",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "name, price and category are required"
    }