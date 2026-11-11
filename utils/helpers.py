# utils/helpers.py


def highest_stock_item(items):
    return max(items, key=lambda i: i.quantity, default=None)


def lowest_stock_item(items):
    return min(items, key=lambda i: i.quantity, default=None)
