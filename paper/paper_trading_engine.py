
"""
Paper Trading Engine
BIST AI LAB v5
"""

from __future__ import annotations

import pandas as pd


class PaperTradingEngine:

    def __init__(self, initial_cash: float = 100000.0):
        self.cash = initial_cash
        self.position = 0.0
        self.history = []

    def on_signal(self, date, signal, price):

        if signal == "BUY" and self.position == 0:
            self.position = self.cash / price
            self.cash = 0.0

        elif signal == "SELL" and self.position > 0:
            self.cash = self.position * price
            self.position = 0.0

        equity = self.cash if self.position == 0 else self.position * price

        self.history.append({
            "Date": date,
            "Signal": signal,
            "Price": float(price),
            "Equity": float(equity),
        })

    def report(self):
        return pd.DataFrame(self.history)
