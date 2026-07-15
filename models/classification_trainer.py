"""
Classification Trainer
BIST AI LAB v4
"""

from __future__ import annotations

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

from models.classifier import Classifier


class ClassificationTrainer:

    def __init__(self):

        self.classifier = Classifier()

    # ==================================================

    def fit(
        self,
        X_train,
        y_train,
    ):

        self.classifier.fit(
            X_train,
            y_train,
        )

        return self

    # ==================================================

    def predict(
        self,
        X,
    ):

        return self.classifier.predict(X)

    # ==================================================

    def predict_proba(
        self,
        X,
    ):

        return self.classifier.predict_proba(X)

    # ==================================================

    def evaluate(
        self,
        y_true,
        y_pred,
    ):

        return {

            "Accuracy": round(
                accuracy_score(
                    y_true,
                    y_pred,
                ),
                4,
            ),

            "Precision": round(
                precision_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0,
                ),
                4,
            ),

            "Recall": round(
                recall_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0,
                ),
                4,
            ),

            "F1": round(
                f1_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0,
                ),
                4,
            ),

            "ConfusionMatrix": confusion_matrix(
                y_true,
                y_pred,
            ).tolist(),

        }

    # ==================================================

    def save(self):

        self.classifier.save()

    # ==================================================

    def load(self):

        self.classifier.load()

        return self
