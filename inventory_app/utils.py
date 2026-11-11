"""utils.py

Small formatting helpers with no dependency on the rest of the app.
"""


def money(amount: float) -> str:
    """Format a Naira amount, e.g. 1608000 -> 'NGN 1,608,000.00'."""
    return f"NGN {amount:,.2f}"
