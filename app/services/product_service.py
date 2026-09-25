products = [
    {
    "id": 1,
    "name": "Laptop",
    "price": 75000,
    "category": "Electronics",
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 2500,
        "category": "Accessories",
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 1500,
        "category": "Accessories",
    },
]


def get_all_products():
    return products

def get_product_by_id(product_id):
    return next(
        (product for product in products if product["id"] == product_id),
        None,
    )

def create_product(name, price, category):
    product = {
        "id": max(product["id"] for product in products) + 1
        if products
        else 1,
        "name": name,
        "price": price,
        "category": category,
    }

    products.append(product)

    return product