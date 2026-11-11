# Inventory Tracker

SEN 401 (Software Configuration Management and Maintenance), Labs 3 and 4.
A shop inventory program that tracks items, quantities and prices and works out the total stock value.

## Versions

| Tag | What changed |
|---|---|
| `v1.0` | Lab 3: console program after corrective, adaptive, perfective and preventive maintenance |
| `v2.0` | Lab 4: re-engineered into modules, data migrated to SQLite, FastAPI REST API, Docker Compose |

## Structure (v2.0)

```
inventory-tracker/
├── inventory_app/
│   ├── models.py        # Item, ItemIn, QuantityUpdate (Pydantic)
│   ├── database.py      # all SQLite access
│   ├── controllers.py   # business rules: totals, highest/lowest, low stock, report
│   ├── utils.py         # money() formatting
│   ├── cli.py           # console report
│   └── api.py           # FastAPI REST API
├── data/
│   ├── inventory.json   # original data (migration source)
│   └── inventory.db     # SQLite database after migration
├── migrate.py           # JSON -> SQLite migration
├── client.py            # HTTP test client for the API
├── app.py               # entry point for the console report
├── Dockerfile
├── docker-compose.yml
├── changelog.txt        # exported git log
├── CSA.md               # configuration status accounting record
└── docs/reverse_engineering.md
```

## Run locally

```bash
pip install -r requirements.txt
python migrate.py                      # JSON -> SQLite
python app.py                          # console report
uvicorn inventory_app.api:app --reload # API on http://localhost:8000/docs
```

## Run with Docker Compose

```bash
docker compose up --build
```

This starts three containers: `migrate` loads the data into SQLite, `api` serves the REST API on port 8000,
and `client` calls the API over the Docker network to check that the services communicate.

## API endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/items` | List all items |
| GET | `/items/{id}` | One item |
| POST | `/items` | Add (or update) an item |
| PUT | `/items/{id}/quantity` | Change an item's quantity |
| DELETE | `/items/{id}` | Remove an item |
| GET | `/low-stock` | Items below 15 units |
| GET | `/report` | Total stock value and other statistics |

## Author

Emmanuel Oyebanji Oyebode (2024/C/SENG/0866)
