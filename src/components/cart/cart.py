from __future__ import annotations

from decimal import Decimal

from src.components.catalog.catalog import Catalog
from src.components.cart.line_items import BundleLineItem, SingleLineItem
from src.interfaces.cart_line import CartLine
from src.interfaces.pricing_strategy import PricingStrategy
from src.components.cart.pricing_strategies import StandardPricingStrategy


class Cart:
    """Shopping cart: aggregate of CartLine objects (Composite at cart boundary)."""

    def __init__(self, pricing: PricingStrategy | None = None) -> None:
        self._lines: list[CartLine] = []
        self._pricing: PricingStrategy = pricing or StandardPricingStrategy()

    def set_pricing_strategy(self, pricing: PricingStrategy) -> None:
        """Swap calculation policy at runtime without rewriting line-item code."""
        self._pricing = pricing

    def add_line(self, line: CartLine) -> None:
        self._lines.append(line)

    def add_product_line(self, catalog: Catalog, product_id: str, quantity: int = 1) -> None:
        """Integration: unit price and identity come from Catalog (single source of truth)."""
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        product = catalog.get_by_id(product_id)
        if product is None:
            raise ValueError(f"Unknown product_id: {product_id}")
        self.add_line(SingleLineItem(product_id, quantity, product.price))

    def add_bundle_line(
        self,
        catalog: Catalog,
        label: str,
        parts: list[tuple[str, int]],
    ) -> None:
        """Build a composite bundle line using catalog-backed prices for each part."""
        children: list[CartLine] = []
        for pid, qty in parts:
            if qty < 1:
                raise ValueError("each bundle part quantity must be at least 1")
            p = catalog.get_by_id(pid)
            if p is None:
                raise ValueError(f"Unknown product_id in bundle: {pid}")
            children.append(SingleLineItem(pid, qty, p.price))
        self.add_line(BundleLineItem(label, children))

    def __iter__(self):
        return iter(self._lines)

    def __len__(self) -> int:
        return len(self._lines)

    def subtotal(self) -> Decimal:
        """Sum of all root line totals (before strategy)."""
        return sum((line.line_total() for line in self._lines), Decimal("0"))

    def total(self) -> Decimal:
        """Final charge using the active PricingStrategy."""
        return self._pricing.apply(self.subtotal())
