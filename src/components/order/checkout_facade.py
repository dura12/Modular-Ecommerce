from __future__ import annotations

from decimal import Decimal
from uuid import uuid4

from src.components.cart.cart import Cart
from src.components.catalog.catalog import Catalog
from src.components.order.order import OrderConfirmation
from src.components.order.order_repository import OrderRepository
from src.interfaces.payment_gateway import IPaymentGateway


class CheckoutFacade:
    """Orchestrates validation, pricing, and payment behind one simple call."""

    def __init__(
        self,
        cart: Cart,
        catalog: Catalog,
        payment_gateway: IPaymentGateway,
        *,
        order_repository: OrderRepository | None = None,
    ) -> None:
        self._cart = cart
        self._catalog = catalog
        self._payment_gateway = payment_gateway
        self._order_repository = order_repository

    def process_checkout(self, user_id: str, currency: str = "USD") -> OrderConfirmation:
        if len(self._cart) == 0:
            raise ValueError("Cannot checkout an empty cart")

        self._validate_cart_items()
        total: Decimal = self._cart.total()
        payment_receipt = self._payment_gateway.process_payment(total, currency)
        order_id = f"ORD-{uuid4().hex[:10].upper()}"

        confirmation = OrderConfirmation(
            order_id=order_id,
            user_id=user_id,
            amount=total,
            currency=currency,
            payment_receipt=payment_receipt,
        )
        if self._order_repository is not None:
            self._order_repository.save(confirmation)
        return confirmation

    def _validate_cart_items(self) -> None:
        for line in self._cart:
            for product_id in line.referenced_product_ids():
                if self._catalog.get_by_id(product_id) is None:
                    raise ValueError(f"Unknown product in cart: {product_id}")

