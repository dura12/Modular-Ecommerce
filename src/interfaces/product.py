from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal


class Product(ABC):
    """Abstract product: shared identity and price; kind-specific behavior in subclasses."""

    def __init__(self, product_id: str, name: str, price: Decimal) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price

    @abstractmethod
    def product_kind(self) -> str:
        """Return a stable label for the product category (e.g. physical vs digital)."""

    @abstractmethod
    def fulfillment_notes(self) -> str:
        """Human-readable fulfillment hint for demos and future checkout logic."""
