import os

from flask import Flask

from app.routes.health import health_bp
from app.routes.orders import orders_bp
from app.routes.products import products_bp


def create_app():
    app = Flask(__name__)

    # Load application configuration from environment variables
    app.config["APP_ENV"] = os.getenv("APP_ENV", "development")
    app.config["LOG_LEVEL"] = os.getenv("LOG_LEVEL", "INFO")
    app.config["FEATURE_PROMOTIONS_ENABLED"] = (
        os.getenv("FEATURE_PROMOTIONS_ENABLED", "false").lower() == "true"
    )

    @app.route("/")
    def home():
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ecommerce Platform</title>
        </head>
        <body>
            <h1>🛒 Ecommerce Platform</h1>
            <h2>Welcome to our Ecommerce Store</h2>
            <p><strong>Version: v2</strong></p>
            <p>Deployment: Rolling Upgrade Demo</p>
            <p>Status: Healthy</p>
        </body>
        </html>
        """

    app.register_blueprint(health_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)