"""
Portfolio Allocation
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class PortfolioAllocation:

    # ==================================================

    def allocate(
        self,
        portfolio: pd.DataFrame,
        capital: float,
    ) -> pd.DataFrame:

        if portfolio.empty:

            return portfolio

        result = portfolio.copy()

        result["Capital"] = (

            result["Weight"] * capital

        ).round(2)

        result["Shares"] = (

            result["Capital"]

            / result["Current"]

        ).astype(int)

        result["Used Capital"] = (

            result["Shares"]

            * result["Current"]

        ).round(2)

        result["Cash"] = (

            result["Capital"]

            - result["Used Capital"]

        ).round(2)

        return result