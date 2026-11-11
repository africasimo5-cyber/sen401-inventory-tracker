# app.py
# reads the inventory and works out the total stock value

from inventory import get_items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        total = total + item["quantity"] * item["price"]
    return total


def main():
    items = get_items()
    print("Inventory")
    for item in items:
        print(item["item_name"], item["quantity"], item["price"])
    print("Total stock value:", total_stock_value(items))
    print("Highest stock:", highest_stock_item(items)["item_name"])
    print("Lowest stock:", lowest_stock_item(items)["item_name"])
    print("Average price:", sum(i["price"] for i in items) / len(items))


main()
