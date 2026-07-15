"""
Model Trainer
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd

from xgboost import XGBRegressor

from config.settings import RANDOM_STATE
from core.model_manager import ModelManager
from models.metrics import Metrics


class Trainer:

    def __init__(self):

        self.manager = ModelManager()

        self.model = XGBRegressor(

            objective="reg:squarederror",

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            subsample=0.8,

            colsample_bytree=0.8,

            random_state=RANDOM_STATE,

            n_jobs=-1,

        )

    # ==================================================

    def fit(
        self,
        X_train,
        y_train,
    ):

        self.model.fit(
            X_train,
            y_train,
        )

        return self

    # ==================================================

    def predict(
        self,
        X,
    ):

        return self.model.predict(X)

    # ==================================================

    def evaluate(
        self,
        y_true,
        y_pred,
    ):

        return Metrics.regression(
            y_true,
            y_pred,
        )

    # ==================================================

    def save(self):

        self.manager.save(
            self.model
        )

    # ==================================================

    def load(self):

        self.model = self.manager.load()

        return self

    # ==================================================

    def exists(self):

        return self.manager.exists()

    # ==================================================

    def feature_importance(
        self,
        feature_names,
    ) -> pd.DataFrame:

        if not hasattr(
            self.model,
            "feature_importances_",
        ):

            return pd.DataFrame()

        return (

            pd.DataFrame(

                {

                    "Feature": feature_names,

                    "Importance": self.model.feature_importances_,

                }

            )

            .sort_values(

                by="Importance",

                ascending=False,

            )

            .reset_index(drop=True)

        )