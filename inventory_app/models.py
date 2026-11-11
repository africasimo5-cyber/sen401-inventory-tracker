"""models.py

Data models. `Item` is what the rest of the program works with; `ItemIn` and
`QuantityUpdate` validate data coming in through the API.
"""

from typing import Optional

from pydantic import BaseModel, Field


class ItemIn(BaseModel):
    """Data needed to create an item."""

    item_name: str = Field(min_length=1, max_length=100)
    quantity: int = Field(ge=0)
    price: float = Field(gt=0, description="Unit price in Naira")


class Item(ItemIn):
    """An item stored in the database."""

    id: Optional[int] = None

    @property
    def value(self) -> float:
        """Stock value of this item (quantity x unit price)."""
        return self.quantity * self.price


class QuantityUpdate(BaseModel):
    """Body for changing the quantity of an existing item."""

    quantity: int = Field(ge=0)
