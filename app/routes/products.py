from flask import Blueprint, jsonify, request

from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
)

products_bp = Blueprint("products", __name__, url_prefix="/api/products")

@products_bp.route("", methods=["GET"])
def list_products():
    return jsonify(get_all_products()), 200

@products_bp.route("", methods=["POST"])
def add_product():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    price = data.get("price")
    category = data.get("category")

    if not name or price is None or not category:
        return jsonify(
            {
                "error": "name, price and category are required"
            }
        ), 400

    product = create_product(name, price, category)

    return jsonify(product), 201


@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = get_product_by_id(product_id)

    if product is None:
        return jsonify(
            {
                "error": "product not found"
            }
        ), 404

    return jsonify(product), 200