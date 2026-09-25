from flask import Blueprint, jsonify, request

from app.services.order_service import (
    create_order,
    get_order_by_id,
)


orders_bp = Blueprint(
    "orders",
    __name__,
    url_prefix="/api/orders",
)


@orders_bp.route("", methods=["POST"])
def add_order():
    data = request.get_json(silent=True) or {}

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if product_id is None or quantity is None:
        return jsonify(
            {
                "error": "product_id and quantity are required"
            }
        ), 400

    if not isinstance(quantity, int) or quantity <= 0:
        return jsonify(
            {
                "error": "quantity must be a positive integer"
            }
        ), 400

    order = create_order(product_id, quantity)

    if order is None:
        return jsonify(
            {
                "error": "product not found"
            }
        ), 400

    return jsonify(order), 201


@orders_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = get_order_by_id(order_id)

    if order is None:
        return jsonify(
            {
                "error": "order not found"
            }
        ), 404

    return jsonify(order), 200