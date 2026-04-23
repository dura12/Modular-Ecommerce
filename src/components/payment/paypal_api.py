"""Fake PayPal-shaped API (different vocabulary from Stripe — needs an adapter)."""

from __future__ import annotations

from decimal import Decimal


def pay(amount: Decimal, currency: str) -> dict[str, str]:
    """Pretend PayPal capture call."""
    return {
        "purchase_unit": "PU-1",
        "capture_id": f"PAY-{currency}-{amount}",
        "state": "COMPLETED",
    }
