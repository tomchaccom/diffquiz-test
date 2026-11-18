def total(items):
    return sum(i["price"] * i["qty"] for i in items)


def item_count(items):
    return sum(i["qty"] for i in items if i["qty"] > 0)


def apply_shipping(subtotal, region="domestic"):
    if subtotal <= 0:
        return 0
    fee = 3000 if region == "domestic" else 15000
    if region == "domestic" and subtotal >= 50000:
        fee = 0
    return subtotal + fee
