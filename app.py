"""app.py

Kept as the entry point so `python app.py` still works after re-engineering.
The real code now lives in the inventory_app package.
"""

from inventory_app.cli import main

if __name__ == "__main__":
    main()
