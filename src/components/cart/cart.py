from __future__ import annotations

from decimal import Decimal

from src.interfaces.cart_line import CartLine


class Cart:
    """Shopping cart: aggregate of CartLine objects (Composite at cart boundary)."""

    def __init__(self) -> None:
        self._lines: list[CartLine] = []

    def add_line(self, line: CartLine) -> None:
        self._lines.append(line)

    def __iter__(self):
        return iter(self._lines)

    def __len__(self) -> int:
        return len(self._lines)

    def subtotal(self) -> Decimal:
        """Sum of all root lines; pricing strategies can wrap this later."""
        return sum((line.line_total() for line in self._lines), Decimal("0"))
