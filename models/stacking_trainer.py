"""
Stacking Trainer
BIST AI LAB v4
"""

from __future__ import annotations

from models.stacking_classifier import (
    StackingClassifierModel,
)

from models.classification_metrics import (
    ClassificationMetrics,
)


class StackingTrainer:

    def __init__(self):

        self.model = StackingClassifierModel()

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

    def evaluate(
        self,
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.evaluate(
            y_true,
            y_pred,
        )