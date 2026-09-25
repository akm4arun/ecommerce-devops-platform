from app.services.product_service import get_product_by_id


orders = []


def create_order(product_id, quantity):
    product = get_product_by_id(product_id)

    if product is None:
        return None

    order = {
        "id": len(orders) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total": product["price"] * quantity,
        "status": "created",
    }

    orders.append(order)

    return order


def get_order_by_id(order_id):
    return next(
        (order for order in orders if order["id"] == order_id),
        None,
    )