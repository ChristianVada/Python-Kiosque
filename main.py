from management.product_handler import *
from management.tab_handler import *
from menu import products

if __name__ == "__main__":
    # print(get_product_by_id(28.1))

    # try:
    #     print(get_product_by_id(28.1))
    # except TypeError as e:
    #     print(e)

    # print(get_products_by_type("drink"))

    # try:
    #     print(get_products_by_type(1))
    # except TypeError as e:
    #     print(e)

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
    }

    # print(add_product([], **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]

    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    # print(calculate_tab(table_1))

    # print(calculate_tab(table_2))

    # print(menu_report())
