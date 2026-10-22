from .models import PRODUCTS


def search_products(query="", category="", sort_by="title"):
    output = []
    for product in PRODUCTS:
        if query.lower() not in product.title.lower():
            continue
        if category and category != product.category:
            continue
        output.append(product)
    if sort_by == "price":
        output.sort(key=lambda p: p.price)
    elif sort_by == "stock":
        output.sort(key=lambda p: p.stock, reverse=True)
    else:
        output.sort(key=lambda p: p.title)
    return output


def inventory_summary():
    result = {}
    for product in PRODUCTS:
        if product.category not in result:
            result[product.category] = {"count": 0, "units": 0, "value": 0}
        result[product.category]["count"] += 1
        result[product.category]["units"] += product.stock
        result[product.category]["value"] += product.stock * product.price
    return result
