"""client.py

Small test client that talks to the API over HTTP. In Docker Compose it runs
in its own container and reaches the API by its service name (http://api:8000),
which proves the containers can communicate.

Usage:  python client.py [base_url]
"""

import json
import os
import sys
import time
import urllib.request

BASE = sys.argv[1] if len(sys.argv) > 1 else os.getenv("API_URL", "http://localhost:8000")


def call(method: str, path: str, body: dict | None = None) -> dict | list:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as resp:
        return json.loads(resp.read() or "null")


def wait_for_api(retries: int = 20) -> None:
    for _ in range(retries):
        try:
            call("GET", "/")
            return
        except OSError:
            time.sleep(1)
    sys.exit(f"API at {BASE} did not respond")


def main() -> None:
    wait_for_api()
    print(f"Connected to {BASE}:", call("GET", "/"))

    items = call("GET", "/items")
    print(f"\nGET /items -> {len(items)} items")
    for i in items:
        print(f"  #{i['id']} {i['item_name']}: {i['quantity']} units")

    new = call("POST", "/items", {"item_name": "Semovita (10kg)", "quantity": 25, "price": 11500})
    print(f"\nPOST /items -> added #{new['id']} {new['item_name']}")

    updated = call("PUT", "/items/4/quantity", {"quantity": 40})
    print(f"PUT /items/4/quantity -> {updated['item_name']} now has {updated['quantity']} units")

    print("\nGET /low-stock ->", [i["item_name"] for i in call("GET", "/low-stock")])
    print("GET /report ->", json.dumps(call("GET", "/report"), indent=2))


if __name__ == "__main__":
    main()
