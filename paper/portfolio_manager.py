
"""
Portfolio Manager
BIST AI LAB v5
"""

from __future__ import annotations


class PortfolioManager:

    def __init__(self, initial_cash: float = 100000.0):
        self.cash = initial_cash
        self.positions = {}

    def buy(self, symbol: str, quantity: float, price: float):
        cost = quantity * price
        if cost > self.cash:
            raise ValueError("Yetersiz bakiye")
        self.cash -= cost
        self.positions[symbol] = self.positions.get(symbol, 0.0) + quantity

    def sell(self, symbol: str, quantity: float, price: float):
        current = self.positions.get(symbol, 0.0)
        if quantity > current:
            raise ValueError("Yetersiz pozisyon")
        self.positions[symbol] = current - quantity
        self.cash += quantity * price
        if self.positions[symbol] == 0:
            del self.positions[symbol]

    def summary(self):
        return {
            "cash": round(self.cash,2),
            "positions": dict(self.positions),
        }
