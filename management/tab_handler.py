from menu import products


def calculate_tab(table):
    subtotal = 0

    for i in table:
        for j in products:
            if j["_id"] == i["_id"]:
                subtotal += j["price"] * i["amount"]

    return f" subtotal: ${round(subtotal, 2)}"


""" 
def calculate_tab(table):
    consomed_products = []

    for i in table:
        for j in products:
            if j["_id"] == i["_id"]:
                consomed_products.append(j)

        for k in consomed_products:
            amout = k["price"] * i["amount"]
            # print(amout)

    print(consomed_products)
 """
