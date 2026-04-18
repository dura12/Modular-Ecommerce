"""Demo: Catalog + Cart; Composite pattern (single lines + bundle) with prices from Catalog."""

from decimal import Decimal

from src.components.cart.cart import Cart
from src.components.cart.pricing_strategies import PercentDiscountPricingStrategy
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

    cart = Cart()
    cart.add_product_line(catalog, "SKU-MUG", quantity=2)
    cart.add_bundle_line(
        catalog,
        "Reader kit",
        [("SKU-MUG", 1), ("SKU-EBOOK", 1)],
    )

    print("\nCart (Composite: singles + bundle)\n")
    for i, line in enumerate(cart, start=1):
        print(f"  Line {i}: {line.describe()} -> {line.line_total()}")
    print(f"\n  Subtotal (lines only): {cart.subtotal()}")
    print(f"  Total (Standard pricing): {cart.total()}")
    cart.set_pricing_strategy(PercentDiscountPricingStrategy(Decimal("10")))
    print(f"  Total (10% off strategy): {cart.total()}")


if __name__ == "__main__":
    main()
