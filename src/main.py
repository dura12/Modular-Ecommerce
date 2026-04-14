"""Demo: Catalog + Cart; Composite pattern (single lines + bundle) with prices from Catalog."""

from decimal import Decimal

from src.components.cart.cart import Cart
from src.components.cart.line_items import BundleLineItem, SingleLineItem
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

    mug = catalog.get_by_id("SKU-MUG")
    ebook = catalog.get_by_id("SKU-EBOOK")
    assert mug is not None and ebook is not None

    cart = Cart()
    cart.add_line(SingleLineItem(mug.product_id, quantity=2, unit_price=mug.price))
    cart.add_line(
        BundleLineItem(
            "Reader kit",
            [
                SingleLineItem(mug.product_id, 1, mug.price),
                SingleLineItem(ebook.product_id, 1, ebook.price),
            ],
        )
    )

    print("\nCart (Composite: singles + bundle)\n")
    for i, line in enumerate(cart, start=1):
        print(f"  Line {i}: {line.describe()} -> {line.line_total()}")
    print(f"\n  Cart subtotal: {cart.subtotal()}")


if __name__ == "__main__":
    main()
