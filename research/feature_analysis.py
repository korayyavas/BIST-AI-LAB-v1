"""
Feature Analysis
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class FeatureAnalysis:

    # ==================================================

    @staticmethod
    def importance(
        trainer,
        feature_names,
    ) -> pd.DataFrame:

        return trainer.feature_importance(
            feature_names
        )

    # ==================================================

    @staticmethod
    def top_features(
        importance: pd.DataFrame,
        top_n: int = 20,
    ) -> pd.DataFrame:

        return (

            importance

            .head(top_n)

            .reset_index(drop=True)

        )

    # ==================================================

    @staticmethod
    def weak_features(
        importance: pd.DataFrame,
        threshold: float = 0.001,
    ) -> pd.DataFrame:

        return (

            importance[

                importance["Importance"] < threshold

            ]

            .reset_index(drop=True)

        )

    # ==================================================

    @staticmethod
    def summary(
        importance: pd.DataFrame,
    ) -> dict:

        return {

            "Feature Count": len(importance),

            "Average Importance": round(

                importance["Importance"].mean(),

                6,

            ),

            "Max Importance": round(

                importance["Importance"].max(),

                6,

            ),

            "Min Importance": round(

                importance["Importance"].min(),

                6,

            ),

        }