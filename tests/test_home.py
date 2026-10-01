from app.main import create_app


def test_homepage():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Ecommerce Platform" in response.data
    assert b"Welcome to our Ecommerce Store" in response.data
    assert b"Version: v2" in response.data
    assert b"Deployment: Blue/Green Demo" in response.data
    assert b"Status: Healthy" in response.data
    assert b"Deployment Color:" in response.data
