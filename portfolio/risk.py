"""
Portfolio Risk
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class PortfolioRisk:

    # ==================================================

    def analyze(
        self,
        portfolio: pd.DataFrame,
    ) -> dict:

        if portfolio.empty:

            return {

                "Positions": 0,

                "Average Risk": 0.0,

                "Average Return": 0.0,

                "Average R/R": 0.0,

                "Average Confidence": 0.0,

            }

        return {

            "Positions": len(portfolio),

            "Average Risk": round(

                portfolio["Risk"].mean(),

                2,

            ),

            "Average Return": round(

                portfolio["Return %"].mean(),

                2,

            ),

            "Average R/R": round(

                portfolio["R/R"].mean(),

                2,

            ),

            "Average Confidence": round(

                portfolio["Confidence"].mean(),

                2,

            ),

        }

    # ==================================================

    def portfolio_score(
        self,
        portfolio: pd.DataFrame,
    ) -> float:

        if portfolio.empty:

            return 0.0

        score = (

            portfolio["Confidence"].mean()

            * 0.40

            +

            portfolio["R/R"].mean() * 20

            +

            (100 - portfolio["Risk"].mean())

            * 0.40

        )

        return round(

            min(score, 100),

            2,

        )