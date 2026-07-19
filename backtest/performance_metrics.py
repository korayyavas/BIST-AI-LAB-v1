"""
Performance Metrics
BIST AI LAB v6
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class PerformanceMetrics:

    @staticmethod
    def calculate(equity):

        if isinstance(equity, pd.DataFrame):

            cols = {c.lower(): c for c in equity.columns}

            if "equity" in cols:
                equity = equity[cols["equity"]].to_numpy()

            elif "value" in cols:
                equity = equity[cols["value"]].to_numpy()

            else:
                equity = (
                    equity.select_dtypes(include=["number"])
                    .iloc[:, -1]
                    .to_numpy()
                )

        equity = np.asarray(equity, dtype=float).flatten()

        if len(equity) < 2:
            raise ValueError("Equity curve must contain at least two observations.")

        returns = np.diff(equity) / equity[:-1]

        total_return = (equity[-1] / equity[0] - 1) * 100

        running_max = np.maximum.accumulate(equity)

        drawdown = (equity - running_max) / running_max

        max_drawdown = drawdown.min() * 100

        sharpe = 0.0

        if returns.std() > 0:
            sharpe = (
                returns.mean() / returns.std()
            ) * np.sqrt(252)

        return {
            "Initial Equity": round(float(equity[0]), 2),
            "Final Equity": round(float(equity[-1]), 2),
            "Total Return %": round(float(total_return), 2),
            "Max Drawdown %": round(float(max_drawdown), 2),
            "Sharpe Ratio": round(float(sharpe), 3),
        }