"""
Backtest Metrics
BIST AI LAB v3
"""

from __future__ import annotations

import math

import pandas as pd


class BacktestMetrics:

    # ==================================================

    @staticmethod
    def total_return(
        returns: pd.Series,
    ) -> float:

        return round(
            returns.sum(),
            2,
        )

    # ==================================================

    @staticmethod
    def average_return(
        returns: pd.Series,
    ) -> float:

        return round(
            returns.mean(),
            2,
        )

    # ==================================================

    @staticmethod
    def win_rate(
        returns: pd.Series,
    ) -> float:

        wins = (returns > 0).sum()

        total = len(returns)

        if total == 0:

            return 0.0

        return round(
            wins / total * 100,
            2,
        )

    # ==================================================

    @staticmethod
    def max_gain(
        returns: pd.Series,
    ) -> float:

        return round(
            returns.max(),
            2,
        )

    # ==================================================

    @staticmethod
    def max_loss(
        returns: pd.Series,
    ) -> float:

        return round(
            returns.min(),
            2,
        )

    # ==================================================

    @staticmethod
    def volatility(
        returns: pd.Series,
    ) -> float:

        return round(
            returns.std(),
            4,
        )

    # ==================================================

    @staticmethod
    def sharpe_ratio(
        returns: pd.Series,
        risk_free_rate: float = 0.0,
    ) -> float:

        excess = returns - risk_free_rate

        std = excess.std()

        if std == 0:

            return 0.0

        return round(
            excess.mean() / std * math.sqrt(252),
            2,
        )