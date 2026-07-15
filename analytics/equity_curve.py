"""
Equity Curve
BIST AI LAB v3.1
"""

from __future__ import annotations

import pandas as pd


class EquityCurve:

    # ==================================================

    @staticmethod
    def build(
        returns: pd.Series,
        initial_capital: float = 100000,
    ) -> pd.DataFrame:

        equity = (

            1 + returns / 100

        ).cumprod()

        equity *= initial_capital

        return pd.DataFrame(

            {

                "Trade": range(

                    1,

                    len(equity) + 1,

                ),

                "Equity": equity.round(2),

            }

        )

    # ==================================================

    @staticmethod
    def returns(
        equity: pd.DataFrame,
    ) -> pd.Series:

        return (

            equity["Equity"]

            .pct_change()

            .fillna(0)

            * 100

        )

    # ==================================================

    @staticmethod
    def high_watermark(
        equity: pd.DataFrame,
    ) -> pd.Series:

        return equity["Equity"].cummax()

    # ==================================================

    @staticmethod
    def drawdown(
        equity: pd.DataFrame,
    ) -> pd.Series:

        hwm = EquityCurve.high_watermark(
            equity
        )

        return (

            (equity["Equity"] - hwm)

            / hwm

            * 100

        ).round(2)

    # ==================================================

    @staticmethod
    def summary(
        equity: pd.DataFrame,
    ) -> dict:

        return {

            "Initial Capital": round(

                equity.iloc[0]["Equity"],

                2,

            ),

            "Final Capital": round(

                equity.iloc[-1]["Equity"],

                2,

            ),

            "Peak Capital": round(

                equity["Equity"].max(),

                2,

            ),

            "Minimum Capital": round(

                equity["Equity"].min(),

                2,

            ),

        }