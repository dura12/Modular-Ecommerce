from __future__ import annotations

from src.components.order.order import OrderConfirmation


class OrderRepository:
    """In-memory persistence for order confirmations (per-user history)."""

    def __init__(self) -> None:
        self._by_user: dict[str, list[OrderConfirmation]] = {}

    def save(self, order: OrderConfirmation) -> None:
        self._by_user.setdefault(order.user_id, []).append(order)

    def list_for_user(self, user_id: str) -> tuple[OrderConfirmation, ...]:
        """Snapshot of confirmations for demos and future DB swap."""
        return tuple(self._by_user.get(user_id, ()))
