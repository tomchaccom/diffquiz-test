def total(items):
    return sum(i["price"] * i["qty"] for i in items)


def discount_rate(subtotal):
    if subtotal >= 100000:
        return 0.1
    if subtotal >= 50000:
        return 0.05
    return 0
