"""database.py

All SQLite access lives here, so no other module writes SQL.
The database path comes from the INVENTORY_DB environment variable so the
same code works locally and inside Docker.
"""

import os
import sqlite3
from contextlib import contextmanager
from typing import Iterator, Optional

from inventory_app.models import Item, ItemIn

DB_PATH: str = os.getenv("INVENTORY_DB", "data/inventory.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT    NOT NULL UNIQUE,
    quantity  INTEGER NOT NULL CHECK (quantity >= 0),
    price     REAL    NOT NULL CHECK (price > 0)
);
"""


@contextmanager
def connect(path: Optional[str] = None) -> Iterator[sqlite3.Connection]:
    """Open a connection, commit on success and always close it."""
    conn = sqlite3.connect(path or DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(path: Optional[str] = None) -> None:
    """Create the items table if it does not exist yet."""
    os.makedirs(os.path.dirname(path or DB_PATH) or ".", exist_ok=True)
    with connect(path) as conn:
        conn.executescript(SCHEMA)


def _to_item(row: sqlite3.Row) -> Item:
    return Item(**dict(row))


def list_items(path: Optional[str] = None) -> list[Item]:
    """Return every item ordered by id."""
    with connect(path) as conn:
        return [_to_item(r) for r in conn.execute("SELECT * FROM items ORDER BY id")]


def get_item(item_id: int, path: Optional[str] = None) -> Optional[Item]:
    """Return one item, or None if the id does not exist."""
    with connect(path) as conn:
        row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        return _to_item(row) if row else None


def upsert_item(item: ItemIn, path: Optional[str] = None) -> Item:
    """Insert an item, or update quantity and price if the name already exists."""
    with connect(path) as conn:
        conn.execute(
            """INSERT INTO items (item_name, quantity, price) VALUES (?, ?, ?)
               ON CONFLICT(item_name) DO UPDATE SET quantity = excluded.quantity, price = excluded.price""",
            (item.item_name, item.quantity, item.price),
        )
        row = conn.execute("SELECT * FROM items WHERE item_name = ?", (item.item_name,)).fetchone()
        return _to_item(row)


def update_quantity(item_id: int, quantity: int, path: Optional[str] = None) -> Optional[Item]:
    """Set a new quantity for an item. Returns the updated item, or None if not found."""
    with connect(path) as conn:
        cur = conn.execute("UPDATE items SET quantity = ? WHERE id = ?", (quantity, item_id))
        if cur.rowcount == 0:
            return None
    return get_item(item_id, path)


def delete_item(item_id: int, path: Optional[str] = None) -> bool:
    """Delete an item. Returns True if something was deleted."""
    with connect(path) as conn:
        return conn.execute("DELETE FROM items WHERE id = ?", (item_id,)).rowcount > 0
