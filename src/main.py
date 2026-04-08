"""Minimal demo: Factory creates Physical vs Digital products without exposing constructors everywhere."""

from decimal import Decimal

from src.components.catalog.factory import ProductFactory, ProductType


def main() -> None:
    mug = ProductFactory.create(
        ProductType.PHYSICAL,
        "SKU-MUG",
        "Ceramic Mug",
        Decimal("12.99"),
        weight_kg=0.35,
    )
    ebook = ProductFactory.create(
        ProductType.DIGITAL,
        "SKU-EBOOK",
        "Clean Code PDF",
        Decimal("29.00"),
        download_url="https://example.com/download/ebook",
    )
    for p in (mug, ebook):
        print(f"{p.name} ({p.product_kind()}): {p.price} — {p.fulfillment_notes()}")


if __name__ == "__main__":
    main()
