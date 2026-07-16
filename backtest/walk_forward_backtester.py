"""
Walk Forward Backtester
BIST AI LAB v4
"""

from __future__ import annotations

import pandas as pd
from sklearn.model_selection import TimeSeriesSplit

from models.classification_metrics import ClassificationMetrics


class WalkForwardBacktester:

    def __init__(self, trainer, n_splits: int = 5):
        self.trainer = trainer
        self.n_splits = n_splits

    def run(self, X: pd.DataFrame, y: pd.Series):
        splitter = TimeSeriesSplit(n_splits=self.n_splits)
        rows = []

        for fold, (train_idx, test_idx) in enumerate(splitter.split(X), start=1):
            X_train = X.iloc[train_idx]
            X_test = X.iloc[test_idx]
            y_train = y.iloc[train_idx]
            y_test = y.iloc[test_idx]

            self.trainer.fit(X_train, y_train)
            pred = self.trainer.predict(X_test)
            m = ClassificationMetrics.evaluate(y_test, pred)

            rows.append({
                "Fold": fold,
                "Accuracy": m["Accuracy"],
                "Precision": m["Precision"],
                "Recall": m["Recall"],
                "F1": m["F1"],
            })

        result = pd.DataFrame(rows)

        summary = {
            "Accuracy": round(result["Accuracy"].mean(), 4),
            "Precision": round(result["Precision"].mean(), 4),
            "Recall": round(result["Recall"].mean(), 4),
            "F1": round(result["F1"].mean(), 4),
        }

        return result, summary
