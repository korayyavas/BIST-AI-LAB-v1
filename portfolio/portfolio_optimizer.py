
"""
Portfolio Optimizer
BIST AI LAB v5
"""

from __future__ import annotations

import pandas as pd

from portfolio.position_sizer import PositionSizer


class PortfolioOptimizer:

    def __init__(self):
        self.sizer = PositionSizer()

    def optimize(
        self,
        trades: pd.DataFrame,
        initial_equity: float = 100000.0,
    ):

        equity = initial_equity
        rows = []

        for _, trade in trades.iterrows():

            info = self.sizer.calculate(
                equity=equity,
                entry_price=float(trade["Entry"]),
                stop_loss=float(trade["StopLoss"]),
            )

            equity -= info["risk_amount"]

            rows.append({
                **trade.to_dict(),
                **info,
                "equity_after": round(equity,2),
            })

        return pd.DataFrame(rows)
