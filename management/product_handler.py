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
