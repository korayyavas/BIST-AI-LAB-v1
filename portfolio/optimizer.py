"""
Portfolio Optimizer
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class PortfolioOptimizer:

    def optimize(
        self,
        screener: pd.DataFrame,
        max_positions: int = 10,
    ) -> pd.DataFrame:

        if screener.empty:

            return pd.DataFrame()

        portfolio = (

            screener

            .sort_values(

                by=[

                    "Signal",

                    "Confidence",

                    "Return %",

                    "R/R",

                ],

                ascending=[

                    True,

                    False,

                    False,

                    False,

                ],

            )

            .head(max_positions)

            .copy()

        )

        weight = round(

            1 / len(portfolio),

            4,

        )

        portfolio["Weight"] = weight

        portfolio["Capital %"] = (

            portfolio["Weight"] * 100

        ).round(2)

        return portfolio.reset_index(
            drop=True
        )