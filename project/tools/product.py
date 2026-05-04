# tools/product.py
def get_product_info(
    product_id=None,
    products=None,
    category=None,
    min_price=None,
    max_price=None,
    name=None,
):
    if products is None:
        products = DEFAULT_PRODUCTS

    if product_id is not None:
        product = products.get(product_id)
        if not product or not matches_filters(
            product, category, min_price, max_price, name
        ):
            return {"status": "error", "message": "Product not found"}
        return {"status": "success", "data": product}

    filtered = [
        p
        for p in products.values()
        if matches_filters(p, category, min_price, max_price, name)
    ]

    return {"status": "success", "data": filtered}


DEFAULT_PRODUCTS = {
    "product1": {"name": "Product 1", "category": "Category A", "price": 10.99},
    "product2": {"name": "Product 2", "category": "Category B", "price": 20.99},
    "product3": {"name": "Product 3", "category": "Category A", "price": 15.99},
}


def matches_filters(product, category, min_price, max_price, name):
    if name and name.lower() not in product["name"].lower():
        return False
    if category and product["category"] != category:
        return False
    if min_price and product["price"] < min_price:
        return False
    if max_price and product["price"] > max_price:
        return False
    return True
