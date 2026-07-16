"""
Classification Validator
BIST AI LAB v4
"""

from __future__ import annotations

import pandas as pd

from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


class ClassificationValidator:

    def __init__(
        self,
        n_splits: int = 5,
    ):
        self.n_splits = n_splits

    def walk_forward(
        self,
        trainer,
        X,
        y,
    ) -> pd.DataFrame:

        tscv = TimeSeriesSplit(
            n_splits=self.n_splits
        )

        rows = []

        for fold, (train_idx, test_idx) in enumerate(
            tscv.split(X),
            start=1,
        ):

            X_train = X.iloc[train_idx]
            X_test = X.iloc[test_idx]

            y_train = y.iloc[train_idx]
            y_test = y.iloc[test_idx]

            trainer.fit(
                X_train,
                y_train,
            )

            pred = trainer.predict(
                X_test,
            )

            rows.append({

                "Fold": fold,

                "Accuracy": round(
                    accuracy_score(
                        y_test,
                        pred,
                    ),
                    4,
                ),

                "Precision": round(
                    precision_score(
                        y_test,
                        pred,
                        average="weighted",
                        zero_division=0,
                    ),
                    4,
                ),

                "Recall": round(
                    recall_score(
                        y_test,
                        pred,
                        average="weighted",
                        zero_division=0,
                    ),
                    4,
                ),

                "F1": round(
                    f1_score(
                        y_test,
                        pred,
                        average="weighted",
                        zero_division=0,
                    ),
                    4,
                ),

            })

        return pd.DataFrame(rows)
