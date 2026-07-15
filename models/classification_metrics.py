"""
Classification Metrics
BIST AI LAB v4
"""

from __future__ import annotations

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


class ClassificationMetrics:

    @staticmethod
    def evaluate(
        y_true,
        y_pred,
    ) -> dict:

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

            "Report": classification_report(
                y_true,
                y_pred,
                zero_division=0,
            ),

        }
