def find_product_by_name(products, name):

    #added strip to get rid of whitespace 
    #added lower to match casing use in loop below
    name = name.lower().strip()
    for product in products:
        #added strip to get rid of whitespace 
        if product["name"].lower().strip() == name:
            return product
    return None


def low_stock_products(products, threshold=5):
    # changed >0 to >=0 because it should include products that are at 0
    return [p for p in products if p["stock"] < threshold and p["stock"] >= 0]


def products_sorted_by_price(products):
    #Sort the products by price.
    products.sort(key=lambda p: p["price"])
    return products


def category_summary(products):
    summary = {}

    for product in products:
        category = product["category"]

        if category not in summary:
            summary[category] = {"product_count": 0, "total_stock": 0}

        # increment the product count by 1 every time that product appears in the products list.
        summary[category]["product_count"] += 1
        # total_stock is the sum of each products individual stock.
        summary[category]["total_stock"] += product["stock"]

    return summary


def revenue_summary(processed_orders):
    total_revenue = 0
    valid_orders = 0

    for order in processed_orders[:1]:
        if order["valid"]:
            valid_orders += 1
            total_revenue += order["subtotal"]

    return {
        "valid_orders": valid_orders,
        "total_revenue": round(total_revenue, 2),
    }
