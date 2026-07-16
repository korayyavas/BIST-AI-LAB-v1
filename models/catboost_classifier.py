"""
CatBoost Classifier
BIST AI LAB v4
"""

from __future__ import annotations

from catboost import CatBoostClassifier

from config.settings import RANDOM_STATE
from core.model_manager import ModelManager


class CatBoostClassifierModel:

    def __init__(self):

        self.manager = ModelManager()

        self.model = CatBoostClassifier(

            loss_function="MultiClass",

            iterations=300,

            learning_rate=0.05,

            depth=6,

            random_seed=RANDOM_STATE,

            verbose=False,

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

        return self.model.predict(X).flatten()

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