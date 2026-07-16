
"""
Paper Broker
BIST AI LAB v5
"""

from __future__ import annotations

from broker.broker_adapter import BrokerAdapter


class PaperBroker(BrokerAdapter):

    def __init__(self, initial_balance: float = 100000.0):
        self.connected = False
        self.balance = initial_balance
        self.positions = {}
        self.orders = []
        self._next_id = 1

    def connect(self):
        self.connected = True
        return True

    def get_balance(self):
        return round(self.balance, 2)

    def get_positions(self):
        return dict(self.positions)

    def place_order(self, symbol, side, quantity, price=None):
        order = {
            "id": self._next_id,
            "symbol": symbol,
            "side": side,
            "quantity": float(quantity),
            "price": None if price is None else float(price),
            "status": "FILLED",
        }
        self._next_id += 1
        self.orders.append(order)

        if side.upper() == "BUY":
            self.positions[symbol] = self.positions.get(symbol, 0.0) + float(quantity)
        elif side.upper() == "SELL":
            self.positions[symbol] = max(
                0.0,
                self.positions.get(symbol, 0.0) - float(quantity),
            )

        return order

    def cancel_order(self, order_id):
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = "CANCELLED"
                return True
        return False

    def disconnect(self):
        self.connected = False
        return True
