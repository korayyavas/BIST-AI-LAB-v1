
"""
Optuna AutoML
BIST AI LAB v4
"""

from __future__ import annotations

import optuna
from xgboost import XGBClassifier
from sklearn.model_selection import TimeSeriesSplit, cross_val_score


class OptunaAutoML:

    def __init__(self, trials: int = 30):
        self.trials = trials
        self.best_model = None
        self.best_params = None

    def _objective(self, trial, X, y):

        params = {
            "objective": "multi:softprob",
            "num_class": 3,
            "eval_metric": "mlogloss",
            "n_estimators": trial.suggest_int("n_estimators", 100, 500),
            "max_depth": trial.suggest_int("max_depth", 3, 8),
            "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2),
            "subsample": trial.suggest_float("subsample", 0.7, 1.0),
            "colsample_bytree": trial.suggest_float("colsample_bytree", 0.7, 1.0),
            "min_child_weight": trial.suggest_int("min_child_weight", 1, 10),
            "gamma": trial.suggest_float("gamma", 0.0, 1.0),
            "random_state": 42,
            "n_jobs": -1,
        }

        model = XGBClassifier(**params)

        cv = TimeSeriesSplit(n_splits=3)

        score = cross_val_score(
            model,
            X,
            y,
            cv=cv,
            scoring="accuracy",
            n_jobs=-1,
        ).mean()

        return score

    def optimize(self, X, y):

        study = optuna.create_study(direction="maximize")

        study.optimize(
            lambda t: self._objective(t, X, y),
            n_trials=self.trials,
        )

        self.best_params = study.best_params

        self.best_model = XGBClassifier(
            objective="multi:softprob",
            num_class=3,
            eval_metric="mlogloss",
            random_state=42,
            n_jobs=-1,
            **self.best_params,
        )

        self.best_model.fit(X, y)

        return self.best_model
