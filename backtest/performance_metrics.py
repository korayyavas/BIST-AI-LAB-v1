
"""
Performance Metrics
BIST AI LAB v4
"""

from __future__ import annotations

import numpy as np


class PerformanceMetrics:

    @staticmethod
    def calculate(equity):

        equity = np.asarray(equity, dtype=float)

        returns = np.diff(equity) / equity[:-1]

        total_return = (equity[-1] / equity[0] - 1) * 100

        running_max = np.maximum.accumulate(equity)
        drawdown = (equity - running_max) / running_max
        max_drawdown = drawdown.min() * 100

        sharpe = 0.0
        if returns.std() > 0:
            sharpe = (
                returns.mean() /
                returns.std()
            ) * np.sqrt(252)

        return {
            "Initial Equity": round(float(equity[0]), 2),
            "Final Equity": round(float(equity[-1]), 2),
            "Total Return %": round(float(total_return), 2),
            "Max Drawdown %": round(float(max_drawdown), 2),
            "Sharpe Ratio": round(float(sharpe), 3),
        }
