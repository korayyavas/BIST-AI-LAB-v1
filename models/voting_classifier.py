"""
Voting Classifier
BIST AI LAB v4
"""

from __future__ import annotations

from sklearn.ensemble import VotingClassifier

from models.classifier import Classifier
from models.lightgbm_classifier import (
    LightGBMClassifierModel,
)
from models.catboost_classifier import (
    CatBoostClassifierModel,
)


class VotingClassifierModel:

    def __init__(self):

        self.xgb = (
            Classifier()
            .model
        )

        self.lgbm = (
            LightGBMClassifierModel()
            .model
        )

        self.cat = (
            CatBoostClassifierModel()
            .model
        )

        self.model = VotingClassifier(

            estimators=[

                ("xgb", self.xgb),

                ("lgbm", self.lgbm),

                ("cat", self.cat),

            ],

            voting="soft",

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

    def predict_proba(
        self,
        X,
    ):

        return self.model.predict_proba(X)