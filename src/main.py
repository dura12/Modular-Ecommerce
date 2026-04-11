"""Demo: Factory creates products; Catalog stores them; Iterator browses without exposing internals."""

from decimal import Decimal

from src.components.catalog.catalog import Catalog
from src.components.catalog.factory import ProductFactory, ProductType


def main() -> None:
    catalog = Catalog()
    catalog.add(
        ProductFactory.create(
            ProductType.PHYSICAL,
            "SKU-MUG",
            "Ceramic Mug",
            Decimal("12.99"),
            weight_kg=0.35,
        )
    )
    catalog.add(
        ProductFactory.create(
            ProductType.DIGITAL,
            "SKU-EBOOK",
            "Clean Code PDF",
            Decimal("29.00"),
            download_url="https://example.com/download/ebook",
        )
    )
    print(f"Catalog: {len(catalog)} products (Iterator pattern)\n")
    for p in catalog:
        print(f"  {p.name} ({p.product_kind()}): {p.price} — {p.fulfillment_notes()}")


if __name__ == "__main__":
    main()
