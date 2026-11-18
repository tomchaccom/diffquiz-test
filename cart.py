def total(items):
    return sum(i["price"] * i["qty"] for i in items)


def is_free_shipping(subtotal, region="domestic"):
    return region == "domestic" and subtotal >= 50000
