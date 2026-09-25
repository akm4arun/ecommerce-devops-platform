from flask import Flask

from app.routes.health import health_bp
from app.routes.orders import orders_bp
from app.routes.products import products_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)