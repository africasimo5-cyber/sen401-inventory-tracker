# app.py
# reads the inventory and works out the total stock value

from inventory import get_items, low_stock_items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        total = total + item.quantity * item.price
    return total


def main():
    items = get_items()
    print("=== Shop Inventory Report ===\n")
    print(f"{'Item':<22}{'Qty':>5}{'Unit price':>14}{'Value':>16}")
    print("-" * 57)
    for item in items:
        value = item.quantity * item.price
        print(f"{item.item_name:<22}{item.quantity:>5}{'NGN ' + format(item.price, ',.2f'):>14}"
              f"{'NGN ' + format(value, ',.2f'):>16}")
    print("-" * 57)
    print(f"Total stock value : NGN {total_stock_value(items):,.2f}")
    print(f"Highest stock     : {highest_stock_item(items).item_name}")
    print(f"Lowest stock      : {lowest_stock_item(items).item_name}")
    print(f"Average unit price: NGN {sum(i.price for i in items) / len(items):,.2f}")
    low = low_stock_items(items)
    if low:
        print("\nLOW STOCK ALERT (below 15 units):")
        for i in low:
            status = "OUT OF STOCK" if i.quantity == 0 else f"{i.quantity} left"
            print(f"  - {i.item_name}: {status}")


if __name__ == "__main__":
    main()
