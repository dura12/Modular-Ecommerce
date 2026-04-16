from __future__ import annotations

from decimal import Decimal

from src.interfaces.cart_line import CartLine
from src.interfaces.pricing_strategy import PricingStrategy
from src.components.cart.pricing_strategies import StandardPricingStrategy


class Cart:
    """Shopping cart: aggregate of CartLine objects (Composite at cart boundary)."""

    def __init__(self, pricing: PricingStrategy | None = None) -> None:
        self._lines: list[CartLine] = []
        self._pricing: PricingStrategy = pricing or StandardPricingStrategy()

    def set_pricing_strategy(self, pricing: PricingStrategy) -> None:
        """Swap calculation policy at runtime without rewriting line-item code."""
        self._pricing = pricing

    def add_line(self, line: CartLine) -> None:
        self._lines.append(line)

    def __iter__(self):
        return iter(self._lines)

    def __len__(self) -> int:
        return len(self._lines)

    def subtotal(self) -> Decimal:
        """Sum of all root line totals (before strategy)."""
        return sum((line.line_total() for line in self._lines), Decimal("0"))

    def total(self) -> Decimal:
        """Final charge using the active PricingStrategy."""
        return self._pricing.apply(self.subtotal())
