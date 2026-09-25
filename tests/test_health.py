from app.main import create_app


def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "ecommerce-api",
        "status": "healthy",
    }


def test_ready():
    app = create_app()
    client = app.test_client()

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "ecommerce-api",
        "status": "ready",
    }