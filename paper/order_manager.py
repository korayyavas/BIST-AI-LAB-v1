
"""
Order Manager
BIST AI LAB v5
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:

    symbol: str
    side: str
    quantity: float
    price: float
    timestamp: str


class OrderManager:

    def __init__(self):
        self.orders = []

    def create_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
    ):

        order = Order(
            symbol=symbol,
            side=side,
            quantity=round(quantity, 4),
            price=round(price, 2),
            timestamp=datetime.now().isoformat(),
        )

        self.orders.append(order)

        return order

    def list_orders(self):
        return self.orders

    def clear(self):
        self.orders.clear()
