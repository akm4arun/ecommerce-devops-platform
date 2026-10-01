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
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }

                .bug-banner {
                    background: #b00020;
                    color: white;
                    padding: 25px;
                    margin-bottom: 30px;
                    border-radius: 8px;
                    font-size: 24px;
                    font-weight: bold;
                }

                .status {
                    color: #b00020;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="bug-banner">
                ⚠️ DEMO BUG — Homepage Deployment Failure
            </div>

            <h1>🛒 Ecommerce Platform</h1>
            <h2>Welcome to our Ecommerce Store</h2>

            <p><strong>Version: v2</strong></p>
            <p>Deployment: Rolling Upgrade Demo</p>
            <p class="status">Status: Healthy</p>

            <p>
                This version represents an intentionally defective release
                for the rollback demonstration.
            </p>
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