"""migrate.py

One-off migration: reads items from data/inventory.json, validates each one
with the ItemIn model and writes it into the SQLite database.
Safe to run more than once (existing items are updated, not duplicated).

Usage:  python migrate.py [path/to/inventory.json]
"""

import json
import os
import sys

from pydantic import ValidationError

from inventory_app import database
from inventory_app.models import ItemIn

SOURCE = os.getenv("INVENTORY_JSON", "data/inventory.json")


def migrate(source: str = SOURCE) -> int:
    """Copy every valid record from the JSON file into SQLite. Returns the number migrated."""
    with open(source, encoding="utf-8") as f:
        records = json.load(f)

    database.init_db()
    migrated = 0
    for record in records:
        try:
            item = database.upsert_item(ItemIn(**record))
            migrated += 1
            print(f"  migrated #{item.id}: {item.item_name}")
        except ValidationError as err:
            print(f"  skipped {record}: {err.errors()[0]['msg']}")
    return migrated


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else SOURCE
    print(f"Migrating {src} -> {database.DB_PATH}")
    count = migrate(src)
    print(f"Done: {count} items in SQLite database.")
