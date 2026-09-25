from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "healthy",
            "service": "ecommerce-api"
        }
    ), 200

@health_bp.route("/ready", methods=["GET"])
def ready():
    return jsonify(
        {
            "status": "ready",
            "service": "ecommerce-api"
        }
    ), 200