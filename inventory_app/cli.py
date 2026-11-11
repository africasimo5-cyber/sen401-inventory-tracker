"""cli.py

Console stock report. Reads from SQLite through database.py and uses the
same controllers as the API.
"""

from inventory_app import database
from inventory_app.controllers import LOW_STOCK_THRESHOLD, build_report, low_stock_items
from inventory_app.models import Item
from inventory_app.utils import money

LINE = "-" * 61


def print_table(items: list[Item]) -> None:
    """Print one row per item."""
    print(f"{'ID':<4}{'Item':<22}{'Qty':>5}{'Unit price':>14}{'Value':>16}")
    print(LINE)
    for i in items:
        print(f"{i.id:<4}{i.item_name:<22}{i.quantity:>5}{money(i.price):>14}{money(i.value):>16}")
    print(LINE)


def main() -> None:
    database.init_db()
    items = database.list_items()
    if not items:
        print("The inventory is empty. Run migrate.py first.")
        return

    report = build_report(items)
    print("=== Shop Inventory Report (SQLite) ===\n")
    print_table(items)
    print(f"Total stock value : {money(report['total_stock_value'])}")
    print(f"Highest stock     : {report['highest_stock_item']}")
    print(f"Lowest stock      : {report['lowest_stock_item']}")
    print(f"Average unit price: {money(report['average_unit_price'])}")
    low = low_stock_items(items)
    if low:
        print(f"\nLOW STOCK ALERT (below {LOW_STOCK_THRESHOLD} units):")
        for i in low:
            print(f"  - {i.item_name}: {'OUT OF STOCK' if i.quantity == 0 else f'{i.quantity} left'}")


if __name__ == "__main__":
    main()
