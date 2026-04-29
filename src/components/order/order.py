from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderConfirmation:
    order_id: str
    user_id: str
    amount: Decimal
    currency: str
    payment_receipt: str

