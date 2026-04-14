from __future__ import annotations

from decimal import Decimal

from src.interfaces.cart_line import CartLine


class SingleLineItem(CartLine):
    """Leaf: one product id, quantity, and unit price (from Catalog when integrated)."""

    def __init__(self, product_id: str, quantity: int, unit_price: Decimal) -> None:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price

    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity

    def describe(self) -> str:
        return f"{self.product_id} x{self.quantity} @ {self.unit_price}"


class BundleLineItem(CartLine):
    """Composite: treats several CartLine entries as one sellable line (e.g. kit)."""

    def __init__(self, label: str, children: list[CartLine]) -> None:
        if not children:
            raise ValueError("bundle must contain at least one child line")
        self.label = label
        self._children = list(children)

    def line_total(self) -> Decimal:
        return sum((c.line_total() for c in self._children), Decimal("0"))

    def describe(self) -> str:
        inner = ", ".join(c.describe() for c in self._children)
        return f"{self.label} [{inner}]"
