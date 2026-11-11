"""controllers.py

Business rules for the inventory. These functions only take and return
data, so both the CLI and the API can use them (no printing, no SQL).
"""

from typing import Optional

from inventory_app.models import Item

LOW_STOCK_THRESHOLD: int = 15


def total_stock_value(items: list[Item]) -> float:
    """Sum of quantity x price for every item."""
    return sum(item.value for item in items)


def highest_stock_item(items: list[Item]) -> Optional[Item]:
    """Item with the most units, or None if there are no items."""
    return max(items, key=lambda i: i.quantity, default=None)


def lowest_stock_item(items: list[Item]) -> Optional[Item]:
    """Item with the fewest units, or None if there are no items."""
    return min(items, key=lambda i: i.quantity, default=None)


def low_stock_items(items: list[Item], threshold: int = LOW_STOCK_THRESHOLD) -> list[Item]:
    """Items with fewer units than the threshold."""
    return [i for i in items if i.quantity < threshold]


def build_report(items: list[Item]) -> dict:
    """Everything the CLI and the /report endpoint show, worked out once."""
    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    return {
        "item_count": len(items),
        "total_stock_value": total_stock_value(items),
        "average_unit_price": (sum(i.price for i in items) / len(items)) if items else 0.0,
        "highest_stock_item": highest.item_name if highest else None,
        "lowest_stock_item": lowest.item_name if lowest else None,
        "low_stock": [i.item_name for i in low_stock_items(items)],
    }
