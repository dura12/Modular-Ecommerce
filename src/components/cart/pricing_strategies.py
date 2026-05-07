from __future__ import annotations

from decimal import Decimal

from src.interfaces.pricing_strategy import PricingStrategy


class StandardPricingStrategy(PricingStrategy):
    """No adjustment: final total equals subtotal."""

    def apply(self, subtotal: Decimal) -> Decimal:
        return subtotal


class PercentDiscountPricingStrategy(PricingStrategy):
    """Example swap-in strategy: percentage off the cart subtotal."""

    def __init__(self, percent_off: Decimal) -> None:
        if percent_off < 0 or percent_off > 100:
            raise ValueError("percent_off must be between 0 and 100")
        self._percent_off = percent_off

    def apply(self, subtotal: Decimal) -> Decimal:
        factor = (Decimal("100") - self._percent_off) / Decimal("100")
        return (subtotal * factor).quantize(Decimal("0.01"))


class FixedDiscountPricingStrategy(PricingStrategy):
    """Flat amount off the cart subtotal (floors at zero)."""

    def __init__(self, amount_off: Decimal) -> None:
        if amount_off < 0:
            raise ValueError("amount_off must be non-negative")
        self._amount_off = amount_off

    def apply(self, subtotal: Decimal) -> Decimal:
        result = subtotal - self._amount_off
        if result < 0:
            return Decimal("0").quantize(Decimal("0.01"))
        return result.quantize(Decimal("0.01"))
