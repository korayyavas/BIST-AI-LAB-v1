"""
AutoML
BIST AI LAB v3
"""

from __future__ import annotations

from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBRegressor

from config.settings import RANDOM_STATE


class AutoML:

    def __init__(

        self,

        cv: int = 3,

        iterations: int = 20,

    ):

        self.cv = cv

        self.iterations = iterations

    # ==================================================

    def optimize(

        self,

        X_train,

        y_train,

    ):

        model = XGBRegressor(

            objective="reg:squarederror",

            random_state=RANDOM_STATE,

            n_jobs=-1,

        )

        params = {

            "n_estimators": [100, 200, 300, 500],

            "learning_rate": [0.01, 0.03, 0.05, 0.1],

            "max_depth": [3, 4, 5, 6, 8],

            "subsample": [0.7, 0.8, 0.9, 1.0],

            "colsample_bytree": [0.7, 0.8, 0.9, 1.0],

            "gamma": [0.0, 0.1, 0.3],

            "min_child_weight": [1, 3, 5],

        }

        search = RandomizedSearchCV(

            estimator=model,

            param_distributions=params,

            n_iter=self.iterations,

            cv=self.cv,

            scoring="neg_mean_absolute_error",

            random_state=RANDOM_STATE,

            n_jobs=-1,

            verbose=1,

            return_train_score=False,

        )

        search.fit(

            X_train,

            y_train,

        )

        self._print_results(search)

        return search.best_estimator_

    # ==================================================

    @staticmethod
    def _print_results(search):

        print("\n" + "=" * 60)
        print("AUTO ML RESULTS")
        print("=" * 60)

        print(
            f"Best Score : {-search.best_score_:.6f}"
        )

        print("\nBest Parameters\n")

        for key, value in search.best_params_.items():

            print(f"{key:20}: {value}")

        print("=" * 60)