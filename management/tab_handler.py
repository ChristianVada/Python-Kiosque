from menu import products


def calculate_tab(table):
    subtotal = 0

    for i in table:
        for j in products:
            if j["_id"] == i["_id"]:
                subtotal += j["price"] * i["amount"]

    format_total = f"${round(subtotal, 2)}"

    dicitionary_response = {"subtotal": format_total}

    return dicitionary_response
