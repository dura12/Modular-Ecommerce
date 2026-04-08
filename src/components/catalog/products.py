from __future__ import annotations

from decimal import Decimal

from src.interfaces.product import Product


class PhysicalProduct(Product):
    """Tangible good: carries shipping-related metadata."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: Decimal,
        *,
        weight_kg: float = 0.0,
    ) -> None:
        super().__init__(product_id, name, price)
        self.weight_kg = weight_kg

    def product_kind(self) -> str:
        return "physical"

    def fulfillment_notes(self) -> str:
        return f"Ship physical item; weight {self.weight_kg} kg"


class DigitalProduct(Product):
    """Downloadable / license-based product."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: Decimal,
        *,
        download_url: str,
    ) -> None:
        super().__init__(product_id, name, price)
        self.download_url = download_url

    def product_kind(self) -> str:
        return "digital"

    def fulfillment_notes(self) -> str:
        return f"Deliver via digital link: {self.download_url}"
