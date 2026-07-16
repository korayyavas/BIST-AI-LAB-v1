"""
Classification AutoML
BIST AI LAB v4
"""

from __future__ import annotations

from sklearn.model_selection import RandomizedSearchCV, TimeSeriesSplit
from xgboost import XGBClassifier


class ClassificationAutoML:

    def __init__(self, n_splits: int = 3, iterations: int = 20):
        self.n_splits = n_splits
        self.iterations = iterations

    def optimize(self, X_train, y_train):

        model = XGBClassifier(
            objective="multi:softprob",
            num_class=3,
            eval_metric="mlogloss",
            random_state=42,
            n_jobs=-1,
        )

        params = {
            "n_estimators": [100, 200, 300, 500],
            "learning_rate": [0.01, 0.03, 0.05, 0.1],
            "max_depth": [3, 4, 5, 6, 8],
            "subsample": [0.7, 0.8, 0.9, 1.0],
            "colsample_bytree": [0.7, 0.8, 0.9, 1.0],
            "gamma": [0, 0.1, 0.3],
            "min_child_weight": [1, 3, 5],
        }

        search = RandomizedSearchCV(
            estimator=model,
            param_distributions=params,
            n_iter=self.iterations,
            scoring="accuracy",
            cv=TimeSeriesSplit(n_splits=self.n_splits),
            random_state=42,
            n_jobs=-1,
            verbose=1,
        )

        search.fit(X_train, y_train)

        return search.best_estimator_
