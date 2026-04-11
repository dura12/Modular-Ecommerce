from __future__ import annotations

from collections.abc import Iterator as IteratorABC
from typing import Optional

from src.interfaces.product import Product


class CatalogIterator:
    """Iterator pattern: traverse products without exposing Catalog's internal list."""

    def __init__(self, products: list[Product]) -> None:
        self._products = products
        self._index = 0

    def __iter__(self) -> CatalogIterator:
        return self

    def __next__(self) -> Product:
        if self._index >= len(self._products):
            raise StopIteration
        item = self._products[self._index]
        self._index += 1
        return item


class Catalog:
    """Stores products; clients iterate via CatalogIterator, not raw list access."""

    def __init__(self) -> None:
        self._products: list[Product] = []

    def add(self, product: Product) -> None:
        self._products.append(product)

    def get_by_id(self, product_id: str) -> Optional[Product]:
        for p in self._products:
            if p.product_id == product_id:
                return p
        return None

    def __iter__(self) -> IteratorABC[Product]:
        return CatalogIterator(self._products)

    def __len__(self) -> int:
        return len(self._products)
