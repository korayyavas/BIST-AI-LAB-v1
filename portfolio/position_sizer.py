
"""
Position Sizer
BIST AI LAB v5
"""

from __future__ import annotations

from portfolio.risk_manager import RiskManager


class PositionSizer:

    def __init__(self):
        self.risk = RiskManager()

    def calculate(
        self,
        equity: float,
        entry_price: float,
        stop_loss: float,
    ):
        result = self.risk.position_size(
            equity=equity,
            entry=entry_price,
            stop_loss=stop_loss,
        )

        result["position_pct"] = round(
            (result["position_value"] / equity) * 100,
            2,
        )

        return result
