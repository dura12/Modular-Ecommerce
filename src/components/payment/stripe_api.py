"""Fake Stripe-shaped API (third-party surface we adapt behind IPaymentGateway)."""

from __future__ import annotations

from decimal import Decimal


def charge(amount: Decimal, currency: str) -> dict[str, str]:
    """Pretend HTTP call to Stripe; returns a dict like real SDK responses."""
    return {
        "object": "charge",
        "id": f"ch_fake_{currency}_{amount}",
        "status": "succeeded",
    }
