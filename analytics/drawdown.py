"""
Drawdown Analysis
BIST AI LAB v3.1
"""

from __future__ import annotations

import pandas as pd


class Drawdown:

    # ==================================================

    @staticmethod
    def equity_curve(
        returns: pd.Series,
        initial_capital: float = 100.0,
    ) -> pd.Series:

        equity = (

            1 + returns / 100

        ).cumprod()

        return equity * initial_capital

    # ==================================================

    @staticmethod
    def drawdown(
        returns: pd.Series,
    ) -> pd.Series:

        equity = Drawdown.equity_curve(
            returns
        )

        peak = equity.cummax()

        dd = (

            (equity - peak)

            / peak

        ) * 100

        return dd

    # ==================================================

    @staticmethod
    def max_drawdown(
        returns: pd.Series,
    ) -> float:

        dd = Drawdown.drawdown(
            returns
        )

        return round(

            dd.min(),

            2,

        )

    # ==================================================

    @staticmethod
    def longest_drawdown(
        returns: pd.Series,
    ) -> int:

        dd = Drawdown.drawdown(
            returns
        )

        longest = 0

        current = 0

        for value in dd:

            if value < 0:

                current += 1

                longest = max(

                    longest,

                    current,

                )

            else:

                current = 0

        return longest

    # ==================================================

    @staticmethod
    def recovery_factor(
        returns: pd.Series,
    ) -> float:

        total_return = (

            (1 + returns / 100)

            .prod()

            - 1

        ) * 100

        max_dd = abs(

            Drawdown.max_drawdown(
                returns
            )

        )

        if max_dd == 0:

            return 0.0

        return round(

            total_return / max_dd,

            2,

        )