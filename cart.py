def total(items, coupon=None):
    subtotal = sum(i["price"] * i["qty"] for i in items if i["qty"] > 0)
    if coupon and subtotal >= coupon["min"]:
        subtotal -= min(coupon["discount"], subtotal)
    return subtotal
