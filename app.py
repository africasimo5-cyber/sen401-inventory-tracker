"""app.py

Reads the inventory from inventory.py and prints a stock report with the
total stock value. Run with:  python app.py
"""

from inventory import Item, LOW_STOCK_THRESHOLD, get_items, low_stock_items
from utils.helpers import highest_stock_item, lowest_stock_item, money

LINE = "-" * 57


def total_stock_value(items: list[Item]) -> float:
    """Sum of quantity x price for every item."""
    return sum(item.value for item in items)


def print_table(items: list[Item]) -> None:
    """Print one row per item with its quantity, unit price and value."""
    print(f"{'Item':<22}{'Qty':>5}{'Unit price':>14}{'Value':>16}")
    print(LINE)
    for item in items:
        print(f"{item.item_name:<22}{item.quantity:>5}{money(item.price):>14}{money(item.value):>16}")
    print(LINE)


def print_alerts(items: list[Item]) -> None:
    """Print a warning for every item that is running low or out of stock."""
    low = low_stock_items(items)
    if not low:
        return
    print(f"\nLOW STOCK ALERT (below {LOW_STOCK_THRESHOLD} units):")
    for item in low:
        status = "OUT OF STOCK" if item.quantity == 0 else f"{item.quantity} left"
        print(f"  - {item.item_name}: {status}")


def main() -> None:
    items = get_items()
    if not items:
        print("The inventory is empty.")
        return

    print("=== Shop Inventory Report ===\n")
    print_table(items)
    print(f"Total stock value : {money(total_stock_value(items))}")
    print(f"Highest stock     : {highest_stock_item(items).item_name}")
    print(f"Lowest stock      : {lowest_stock_item(items).item_name}")
    print(f"Average unit price: {money(sum(i.price for i in items) / len(items))}")
    print_alerts(items)


if __name__ == "__main__":
    main()
