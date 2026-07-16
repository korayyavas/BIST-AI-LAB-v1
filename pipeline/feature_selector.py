"""
Feature Selector
BIST AI LAB v4
"""

from __future__ import annotations

import pandas as pd

from sklearn.feature_selection import (
    SelectFromModel,
)

from xgboost import XGBClassifier


class FeatureSelector:

    def __init__(
        self,
        threshold="median",
    ):

        self.threshold = threshold

        self.selector = None

        self.selected_features = None

    # ==================================================

    def fit(

        self,

        X: pd.DataFrame,

        y,

    ):

        model = XGBClassifier(

            objective="multi:softprob",

            num_class=3,

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            random_state=42,

            eval_metric="mlogloss",

            n_jobs=-1,

        )

        model.fit(

            X,

            y,

        )

        self.selector = SelectFromModel(

            estimator=model,

            threshold=self.threshold,

            prefit=True,

        )

        self.selected_features = list(

            X.columns[

                self.selector.get_support()

            ]

        )

        return self

    # ==================================================

    def transform(

        self,

        X: pd.DataFrame,

    ) -> pd.DataFrame:

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

    def get_features(

        self,

    ):

        return self.selected_features

    # ==================================================

    def feature_count(

        self,

    ):

        return len(

            self.selected_features

        )