from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal


class PricingStrategy(ABC):
    """Strategy: turn raw cart subtotal into final charge without changing Cart line logic."""

    @abstractmethod
    def apply(self, subtotal: Decimal) -> Decimal:
        """Return final total given the sum of all line totals."""
