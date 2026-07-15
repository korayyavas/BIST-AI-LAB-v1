"""
Prediction Pipeline
BIST AI LAB v3
"""

import pandas as pd


class PredictionPipeline:
    """
    Prepares data for live prediction.
    """

    def prepare(
        self,
        df: pd.DataFrame,
        feature_columns: list[str],
    ) -> pd.DataFrame:

        missing = [
            col
            for col in feature_columns
            if col not in df.columns
        ]

        if missing:

            raise ValueError(
                f"Eksik feature'lar: {missing}"
            )

        X = df[feature_columns].copy()

        return X.tail(1)

    # -----------------------------------------

    def predict(
        self,
        predictor,
        X,
    ):

        prediction = predictor.predict(X)

        return float(prediction[0])