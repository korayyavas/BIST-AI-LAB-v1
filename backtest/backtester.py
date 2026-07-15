"""
Backtester
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class Backtester:

    # ==================================================

    def run(
        self,
        df: pd.DataFrame,
        return_column: str = "Return %",
    ) -> dict:

        if df.empty:

            return {

                "Trades": 0,

                "Wins": 0,

                "Losses": 0,

                "Win Rate": 0.0,

                "Average Return": 0.0,

                "Total Return": 0.0,

                "Best Trade": 0.0,

                "Worst Trade": 0.0,

            }

        returns = df[return_column].astype(float)

        wins = (returns > 0).sum()

        losses = (returns <= 0).sum()

        return {

            "Trades": len(df),

            "Wins": int(wins),

            "Losses": int(losses),

            "Win Rate": round(

                wins / len(df) * 100,

                2,

            ),

            "Average Return": round(

                returns.mean(),

                2,

            ),

            "Total Return": round(

                returns.sum(),

                2,

            ),

            "Best Trade": round(

                returns.max(),

                2,

            ),

            "Worst Trade": round(

                returns.min(),

                2,

            ),

        }