"""
Trading Strategy
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class Strategy:

    # ==================================================

    def generate(
        self,
        df: pd.DataFrame,
        buy_threshold: float = 3.0,
        sell_threshold: float = -3.0,
    ) -> pd.DataFrame:

        result = df.copy()

        signals = []

        positions = []

        position = 0

        for value in result["Return %"]:

            if value >= buy_threshold:

                signal = "BUY"

                position = 1

            elif value <= sell_threshold:

                signal = "SELL"

                position = 0

            else:

                signal = "HOLD"

            signals.append(signal)

            positions.append(position)

        result["Signal"] = signals

        result["Position"] = positions

        return result

    # ==================================================

    def trades(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        trades = df[

            df["Signal"] != "HOLD"

        ].copy()

        trades.reset_index(

            drop=True,

            inplace=True,

        )

        return trades