# inventory.py
# list of items in the shop

from dataclasses import dataclass


@dataclass
class Item:
    item_name: str
    quantity: int
    price: float


items: list[Item] = [
    Item("Rice (50kg bag)", 12, 78000),
    Item("Groundnut oil (5L)", 20, 14500),
    Item("Indomie (carton)", 35, 9800),
    Item("Sugar (1kg)", 0, 1700),
    Item("Peak milk (tin)", 60, 650),
]


def get_items() -> list[Item]:
    return items


def low_stock_items(items: list[Item], threshold: int = 15) -> list[Item]:
    return [i for i in items if i.quantity < threshold]
