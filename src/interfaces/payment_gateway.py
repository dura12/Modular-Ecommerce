from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal


class IPaymentGateway(ABC):
    """Internal contract: checkout depends on this, not on Stripe/PayPal specifics."""

    @abstractmethod
    def process_payment(self, amount: Decimal, currency: str) -> str:
        """Charge the customer; return a provider-scoped confirmation id string."""
