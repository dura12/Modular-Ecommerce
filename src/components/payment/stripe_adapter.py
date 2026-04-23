from __future__ import annotations

from decimal import Decimal

from src.interfaces.payment_gateway import IPaymentGateway
from src.components.payment import stripe_api


class StripePaymentAdapter(IPaymentGateway):
    """Adapter: translate process_payment to stripe_api.charge shape."""

    def process_payment(self, amount: Decimal, currency: str) -> str:
        result = stripe_api.charge(amount, currency)
        return f"stripe:{result['id']}"
