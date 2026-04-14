from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal


class CartLine(ABC):
    """Composite participant: leaf (single SKU) or composite (bundle of lines)."""

    @abstractmethod
    def line_total(self) -> Decimal:
        """Monetary total for this line (and nested lines for bundles)."""

    @abstractmethod
    def describe(self) -> str:
        """Short label for demos and future receipts."""
