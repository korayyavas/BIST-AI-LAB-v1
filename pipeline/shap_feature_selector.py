"""
SHAP Feature Selector
BIST AI LAB v4
"""

from __future__ import annotations

import pandas as pd
import shap

from xgboost import XGBClassifier


class ShapFeatureSelector:

    def __init__(
        self,
        top_n: int = 25,
    ):

        self.top_n = top_n

        self.selected_features = []

        self.model = XGBClassifier(

            objective="multi:softprob",

            num_class=3,

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            random_state=42,

            eval_metric="mlogloss",

            n_jobs=-1,

        )

    # ==================================================

    def fit(
        self,
        X: pd.DataFrame,
        y,
    ):

        self.model.fit(
            X,
            y,
        )

        explainer = shap.TreeExplainer(
            self.model,
        )

        shap_values = explainer.shap_values(
            X,
        )

        if isinstance(
            shap_values,
            list,
        ):

            importance = sum(

                abs(v).mean(axis=0)

                for v in shap_values

            ) / len(shap_values)

        else:

            import numpy as np

            if isinstance(shap_values, list):

                importance = np.mean(
                    [
                        np.abs(v).mean(axis=0)
                        for v in shap_values
                    ],
                    axis=0,
                )

            else:

                values = np.array(shap_values)

                if values.ndim == 3:

                    importance = np.abs(values).mean(
                        axis=(0, 2),
                    )

                else:

                    importance = np.abs(values).mean(
                        axis=0,
                    )

        importance = pd.Series(

            importance,

            index=X.columns,

        )

        importance = importance.sort_values(

            ascending=False,

        )

        self.selected_features = list(

            importance.head(

                self.top_n,

            ).index

        )

        return self

    # ==================================================

    def transform(
        self,
        X: pd.DataFrame,
    ):

        return X[

            self.selected_features

        ].copy()

    # ==================================================

    def fit_transform(
        self,
        X,
        y,
    ):

        self.fit(
            X,
            y,
        )

        return self.transform(
            X,
        )

    # ==================================================

    def get_features(self):

        return self.selected_features

    # ==================================================

    def feature_count(self):

        return len(
            self.selected_features
        )

    # ==================================================

    def importance_table(
        self,
        X,
    ):

        return pd.DataFrame(

            {

                "Feature": self.selected_features,

            }

        )