from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    for i in products:
        if i["_id"] == id:
            return i
    return {}


def get_products_by_type(type: str):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    newList = []

    for i in products:
        if i["type"] == type:
            newList.append(i)
    return newList


def add_product(list, **kwargs):
    # find_the_biggest_id = max(list, key=lambda x: x["_id"])

    max_id = None

    if len(list) != 0:
        for i in list:
            if max_id is None or i["_id"] > max_id:
                max_id = i["_id"]

        new_id = max_id + 1

        new_product = {"_id": new_id, **kwargs}

        list.append(new_product)

        return new_product

    else:
        new_product = {"_id": 1, **kwargs}
        list.append(new_product)
        return new_product


def menu_report():
    product_count = len(products)

    average_price = sum(i["price"] for i in products) / product_count

    type_counts = {
        "fruit": len(get_products_by_type("fruit")),
        "vegetable": len(get_products_by_type("vegetable")),
        "bakery": len(get_products_by_type("bakery")),
    }

    most_common_type = max(type_counts, key=type_counts.get)

    return f"Products Count: {product_count} - Average Price: ${round(average_price, 2)} - Most Common Type: {most_common_type}"
