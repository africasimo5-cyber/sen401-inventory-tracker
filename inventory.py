"""inventory.py

Data module for the Inventory Tracker. Defines the Item record and holds
the shop's current stock.
"""

from dataclasses import dataclass

LOW_STOCK_THRESHOLD: int = 15  # items with fewer units than this trigger an alert


@dataclass
class Item:
    """One product in the shop."""

    item_name: str
    quantity: int
    price: float  # unit price in Naira

    @property
    def value(self) -> float:
        """Stock value of this item (quantity x unit price)."""
        return self.quantity * self.price


_items: list[Item] = [
    Item("Rice (50kg bag)", 12, 78000),
    Item("Groundnut oil (5L)", 20, 14500),
    Item("Indomie (carton)", 35, 9800),
    Item("Sugar (1kg)", 0, 1700),
    Item("Peak milk (tin)", 60, 650),
]


def get_items() -> list[Item]:
    """Return a copy of the inventory list."""
    return list(_items)


def low_stock_items(items: list[Item], threshold: int = LOW_STOCK_THRESHOLD) -> list[Item]:
    """Return the items whose quantity is below the threshold."""
    return [i for i in items if i.quantity < threshold]
