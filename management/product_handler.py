from menu import products


def get_product_by_id(id):
    for i in products:
        if i["_id"] == id:
            return i
    return {}


def get_products_by_type(type):
    newList = []

    for i in products:
        if i["type"] == type:
            newList.append(i)
    return newList
