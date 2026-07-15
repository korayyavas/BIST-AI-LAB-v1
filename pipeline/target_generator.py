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
        up_threshold: float = 0.02,
        down_threshold: float = -0.02,
    ):

        self.prediction_days = prediction_days
        self.up_threshold = up_threshold
        self.down_threshold = down_threshold

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
            .sub(1.0)
        )

        df["FUTURE_RETURN"] = future_return

        df["TARGET"] = 1

        df.loc[
            future_return >= self.up_threshold,
            "TARGET",
        ] = 2

        df.loc[
            future_return <= self.down_threshold,
            "TARGET",
        ] = 0

        return df.dropna().reset_index(drop=True)

    # ==================================================

    @staticmethod
    def label_name(label: int) -> str:

        mapping = {
            0: "SELL",
            1: "HOLD",
            2: "BUY",
        }

        return mapping.get(label, "UNKNOWN")

    # ==================================================

    @staticmethod
    def probabilities_to_signal(
        probabilities,
    ) -> dict:

        labels = ["SELL", "HOLD", "BUY"]

        idx = int(probabilities.argmax())

        return {
            "signal": labels[idx],
            "confidence": round(
                float(probabilities[idx]) * 100,
                2,
            ),
            "sell_probability": round(float(probabilities[0]) * 100, 2),
            "hold_probability": round(float(probabilities[1]) * 100, 2),
            "buy_probability": round(float(probabilities[2]) * 100, 2),
        }
