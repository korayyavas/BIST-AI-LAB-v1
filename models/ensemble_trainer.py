"""
Ensemble Trainer
BIST AI LAB v4
"""

from __future__ import annotations

from models.voting_classifier import (
    VotingClassifierModel,
)

from models.classification_metrics import (
    ClassificationMetrics,
)


class EnsembleTrainer:

    def __init__(self):

        self.model = VotingClassifierModel()

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