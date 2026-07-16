"""
Stacking Classifier
BIST AI LAB v4
"""

from __future__ import annotations

from sklearn.ensemble import (
    StackingClassifier,
    RandomForestClassifier,
)

from sklearn.linear_model import LogisticRegression

from models.classifier import Classifier
from models.lightgbm_classifier import (
    LightGBMClassifierModel,
)
from models.catboost_classifier import (
    CatBoostClassifierModel,
)


class StackingClassifierModel:

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

        self.rf = RandomForestClassifier(

            n_estimators=300,

            random_state=42,

            n_jobs=-1,

        )

        self.model = StackingClassifier(

            estimators=[

                ("xgb", self.xgb),

                ("lgbm", self.lgbm),

                ("cat", self.cat),

                ("rf", self.rf),

            ],

            final_estimator=LogisticRegression(

                max_iter=500,

            ),

            stack_method="predict_proba",

            passthrough=False,

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