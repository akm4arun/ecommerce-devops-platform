from app.main import create_app


def test_create_order():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/orders",
        json={
            "product_id": 1,
            "quantity": 2,
        },
    )

    assert response.status_code == 201

    order = response.get_json()

    assert order["id"] == 1
    assert order["product_id"] == 1
    assert order["quantity"] == 2
    assert order["total"] == 150000
    assert order["status"] == "created"


def test_get_order():
    app = create_app()
    client = app.test_client()

    client.post(
        "/api/orders",
        json={
            "product_id": 1,
            "quantity": 2,
        },
    )

    response = client.get("/api/orders/1")

    assert response.status_code == 200

    order = response.get_json()

    assert order["id"] == 1
    assert order["product_id"] == 1
    assert order["quantity"] == 2


def test_create_order_invalid_product():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/orders",
        json={
            "product_id": 999,
            "quantity": 1,
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "product not found"
    }


def test_create_order_invalid_quantity():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/api/orders",
        json={
            "product_id": 1,
            "quantity": 0,
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "quantity must be a positive integer"
    }


def test_get_order_not_found():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/orders/999")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "order not found"
    }