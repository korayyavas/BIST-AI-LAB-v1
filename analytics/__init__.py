"""
Performance Metrics
BIST AI LAB v3.1
"""

from __future__ import annotations

import math

import pandas as pd


class Performance:

    # ==================================================

    @staticmethod
    def total_return(
        returns: pd.Series,
    ) -> float:

        if returns.empty:

            return 0.0

        return round(

            returns.sum(),

            2,

        )

    # ==================================================

    @staticmethod
    def average_return(
        returns: pd.Series,
    ) -> float:

        if returns.empty:

            return 0.0

        return round(

            returns.mean(),

            2,

        )

    # ==================================================

    @staticmethod
    def annual_return(
        returns: pd.Series,
        periods: int = 252,
    ) -> float:

        if returns.empty:

            return 0.0

        cumulative = (

            1 + returns / 100

        ).prod()

        years = max(

            len(returns) / periods,

            1 / periods,

        )

        annual = (

            cumulative ** (1 / years)

        ) - 1

        return round(

            annual * 100,

            2,

        )

    # ==================================================

    @staticmethod
    def volatility(
        returns: pd.Series,
        periods: int = 252,
    ) -> float:

        if returns.empty:

            return 0.0

        value = (

            returns.std()

            * math.sqrt(periods)

        )

        return round(

            value,

            2,

        )

    # ==================================================

    @staticmethod
    def win_rate(
        returns: pd.Series,
    ) -> float:

        if returns.empty:

            return 0.0

        wins = (

            returns > 0

        ).sum()

        return round(

            wins / len(returns) * 100,

            2,

        )

    # ==================================================

    @staticmethod
    def expectancy(
        returns: pd.Series,
    ) -> float:

        if returns.empty:

            return 0.0

        wins = returns[

            returns > 0

        ]

        losses = returns[

            returns <= 0

        ]

        avg_win = (

            wins.mean()

            if len(wins)

            else 0

        )

        avg_loss = (

            abs(losses.mean())

            if len(losses)

            else 0

        )

        win_rate = (

            len(wins)

            / len(returns)

        )

        loss_rate = 1 - win_rate

        expectancy = (

            win_rate * avg_win

            -

            loss_rate * avg_loss

        )

        return round(

            expectancy,

            2,

        )