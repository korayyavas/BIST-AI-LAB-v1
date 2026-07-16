"""
Target Generator
BIST AI LAB v4
"""

from __future__ import annotations

import pandas as pd


class TargetGenerator:

    def __init__(
        self,
        prediction_days: int = 5,
    ):

        self.prediction_days = prediction_days

    # ==================================================

    def transform(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = df.copy()

        future_return = (

            df["Close"]

            .shift(-self.prediction_days)

            .div(df["Close"])

            .sub(1)

        )

        df["FUTURE_RETURN"] = future_return

        q1 = future_return.quantile(0.33)

        q2 = future_return.quantile(0.66)

        df["TARGET"] = 1

        df.loc[
            future_return <= q1,
            "TARGET",
        ] = 0

        df.loc[
            future_return >= q2,
            "TARGET",
        ] = 2

        return (

            df

            .dropna()

            .reset_index(drop=True)

        )

    # ==================================================

    @staticmethod
    def label_name(
        label: int,
    ):

        labels = {

            0: "SELL",

            1: "HOLD",

            2: "BUY",

        }

        return labels[label]

    # ==================================================

    @staticmethod
    def probabilities_to_signal(
        probabilities,
    ):

        labels = [

            "SELL",

            "HOLD",

            "BUY",

        ]

        idx = probabilities.argmax()

        return {

            "signal": labels[idx],

            "confidence": round(
                float(probabilities[idx]) * 100,
                2,
            ),

            "sell_probability": round(
                float(probabilities[0]) * 100,
                2,
            ),

            "hold_probability": round(
                float(probabilities[1]) * 100,
                2,
            ),

            "buy_probability": round(
                float(probabilities[2]) * 100,
                2,
            ),

        }