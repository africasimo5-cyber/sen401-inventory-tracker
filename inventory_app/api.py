"""api.py

REST API for the inventory, built with FastAPI.
Run locally with:  uvicorn inventory_app.api:app --reload
Interactive docs:  http://localhost:8000/docs
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from inventory_app import database
from inventory_app.controllers import build_report, low_stock_items
from inventory_app.models import Item, ItemIn, QuantityUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init_db()  # make sure the table exists before serving requests
    yield


app = FastAPI(title="Inventory Tracker API", version="2.0", lifespan=lifespan)


@app.get("/")
def health() -> dict:
    """Simple check that the API is running."""
    return {"status": "ok", "service": "inventory-api", "version": "2.0"}


@app.get("/items", response_model=list[Item])
def get_items() -> list[Item]:
    return database.list_items()


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = database.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def add_item(item: ItemIn) -> Item:
    return database.upsert_item(item)


@app.put("/items/{item_id}/quantity", response_model=Item)
def set_quantity(item_id: int, body: QuantityUpdate) -> Item:
    item = database.update_quantity(item_id, body.quantity)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{item_id}", status_code=204)
def remove_item(item_id: int) -> None:
    if not database.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/low-stock", response_model=list[Item])
def low_stock() -> list[Item]:
    return low_stock_items(database.list_items())


@app.get("/report")
def report() -> dict:
    return build_report(database.list_items())
