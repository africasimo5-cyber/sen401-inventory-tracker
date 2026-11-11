"""utils/helpers.py

Helper functions for the Inventory Tracker.
"""

from typing import Optional

from inventory import Item


def highest_stock_item(items: list[Item]) -> Optional[Item]:
    """Item with the most units in stock, or None if the list is empty."""
    return max(items, key=lambda i: i.quantity, default=None)


def lowest_stock_item(items: list[Item]) -> Optional[Item]:
    """Item with the fewest units in stock, or None if the list is empty."""
    return min(items, key=lambda i: i.quantity, default=None)


def money(amount: float) -> str:
    """Format a Naira amount, e.g. 1608000 -> 'NGN 1,608,000.00'."""
    return f"NGN {amount:,.2f}"
