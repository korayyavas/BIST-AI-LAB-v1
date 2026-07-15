"""
Predictor
BIST AI LAB v3
"""

from __future__ import annotations

from core.model_manager import ModelManager


class Predictor:

    def __init__(self):

        self.manager = ModelManager()

        self.model = None

        self.load()

    # ==================================================

    def load(self):

        self.model = self.manager.load()

        return self

    # ==================================================

    def reload(self):

        return self.load()

    # ==================================================

    def predict(
        self,
        X,
    ):

        return self.model.predict(X)

    # ==================================================

    def predict_one(
        self,
        X,
    ) -> float:

        return float(

            self.predict(X)[0]

        )

    # ==================================================

    def is_loaded(self):

        return self.model is not None