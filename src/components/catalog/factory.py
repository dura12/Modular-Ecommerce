from __future__ import annotations

from decimal import Decimal
from enum import Enum

from src.interfaces.product import Product
from src.components.catalog.products import DigitalProduct, PhysicalProduct


class ProductType(Enum):
    PHYSICAL = "physical"
    DIGITAL = "digital"


class ProductFactory:
    """Factory: centralizes creation of Product subclasses (CBSE — open for new kinds)."""

    @staticmethod
    def create(
        product_type: ProductType,
        product_id: str,
        name: str,
        price: Decimal,
        *,
        weight_kg: float | None = None,
        download_url: str | None = None,
    ) -> Product:
        if product_type is ProductType.PHYSICAL:
            return PhysicalProduct(
                product_id,
                name,
                price,
                weight_kg=weight_kg if weight_kg is not None else 0.0,
            )
        if product_type is ProductType.DIGITAL:
            if not download_url:
                raise ValueError("Digital products require download_url")
            return DigitalProduct(product_id, name, price, download_url=download_url)
        raise ValueError(f"Unsupported product type: {product_type!r}")
