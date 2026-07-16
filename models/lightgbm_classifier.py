"""
LightGBM Classifier
BIST AI LAB v4
"""

from __future__ import annotations

from lightgbm import LGBMClassifier

from config.settings import RANDOM_STATE
from core.model_manager import ModelManager


class LightGBMClassifierModel:

    def __init__(self):

        self.manager = ModelManager()

        self.model = LGBMClassifier(

            objective="multiclass",

            num_class=3,

            n_estimators=300,

            learning_rate=0.05,

            max_depth=6,

            subsample=0.8,

            colsample_bytree=0.8,

            random_state=RANDOM_STATE,

            verbosity=-1,

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

    # ==================================================

    def save(self):

        self.manager.save_classifier(
            self.model,
        )

    # ==================================================

    def load(self):

        self.model = (
            self.manager.load_classifier()
        )

        return self