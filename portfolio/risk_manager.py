
"""
Risk Manager
BIST AI LAB v5
"""

from __future__ import annotations


class RiskManager:

    def __init__(
        self,
        risk_per_trade: float = 0.01,
        max_position_size: float = 0.10,
    ):
        self.risk_per_trade = risk_per_trade
        self.max_position_size = max_position_size

    def position_size(self, equity: float, entry: float, stop_loss: float):

        risk_amount = equity * self.risk_per_trade
        stop_distance = max(abs(entry - stop_loss), 1e-9)

        shares = risk_amount / stop_distance
        value = shares * entry

        max_value = equity * self.max_position_size

        if value > max_value:
            value = max_value
            shares = value / entry

        return {
            "shares": round(shares, 4),
            "position_value": round(value, 2),
            "risk_amount": round(risk_amount, 2),
        }
