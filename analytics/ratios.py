"""
Performance Ratios
BIST AI LAB v3.1
"""

from __future__ import annotations

import math

import pandas as pd

from analytics.performance import Performance
from analytics.drawdown import Drawdown


class Ratios:

    # ==================================================

    @staticmethod
    def sharpe_ratio(
        returns: pd.Series,
        risk_free_rate: float = 0.0,
        periods: int = 252,
    ) -> float:

        if returns.empty:

            return 0.0

        excess = returns - risk_free_rate

        std = excess.std()

        if std == 0:

            return 0.0

        sharpe = (

            excess.mean()

            / std

        ) * math.sqrt(periods)

        return round(

            sharpe,

            2,

        )

    # ==================================================

    @staticmethod
    def sortino_ratio(
        returns: pd.Series,
        risk_free_rate: float = 0.0,
        periods: int = 252,
    ) -> float:

        if returns.empty:

            return 0.0

        excess = returns - risk_free_rate

        downside = excess[

            excess < 0

        ]

        if len(downside) == 0:

            return 0.0

        downside_std = downside.std()

        if downside_std == 0:

            return 0.0

        sortino = (

            excess.mean()

            / downside_std

        ) * math.sqrt(periods)

        return round(

            sortino,

            2,

        )

    # ==================================================

    @staticmethod
    def calmar_ratio(
        returns: pd.Series,
    ) -> float:

        annual = Performance.annual_return(
            returns
        )

        drawdown = abs(

            Drawdown.max_drawdown(
                returns
            )

        )

        if drawdown == 0:

            return 0.0

        return round(

            annual / drawdown,

            2,

        )

    # ==================================================

    @staticmethod
    def gain_to_pain_ratio(
        returns: pd.Series,
    ) -> float:

        gains = returns[

            returns > 0

        ].sum()

        losses = abs(

            returns[

                returns < 0

            ].sum()

        )

        if losses == 0:

            return 0.0

        return round(

            gains / losses,

            2,

        )

    # ==================================================

    @staticmethod
    def profit_factor(
        returns: pd.Series,
    ) -> float:

        gains = returns[

            returns > 0

        ].sum()

        losses = abs(

            returns[

                returns < 0

            ].sum()

        )

        if losses == 0:

            return 0.0

        return round(

            gains / losses,

            2,

        )