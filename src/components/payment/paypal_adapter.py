from __future__ import annotations

from decimal import Decimal

from src.interfaces.payment_gateway import IPaymentGateway
from src.components.payment import paypal_api


class PayPalPaymentAdapter(IPaymentGateway):
    """Adapter: translate process_payment to paypal_api.pay vocabulary."""

    def process_payment(self, amount: Decimal, currency: str) -> str:
        result = paypal_api.pay(amount, currency)
        return f"paypal:{result['capture_id']}"
