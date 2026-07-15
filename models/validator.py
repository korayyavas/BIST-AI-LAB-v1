"""
Validator
BIST AI LAB v3
"""

from __future__ import annotations

import math
import pandas as pd

from sklearn.model_selection import (
    TimeSeriesSplit,
    train_test_split,
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from config.settings import (
    TEST_SIZE,
    RANDOM_STATE,
)


class Validator:

    def __init__(
        self,
        n_splits: int = 5,
    ):

        self.n_splits = n_splits

    # ==================================================

    def train_test_split(
        self,
        X,
        y,
    ):

        return train_test_split(

            X,

            y,

            test_size=TEST_SIZE,

            shuffle=False,

            random_state=RANDOM_STATE,

        )

    # ==================================================

    def walk_forward(
        self,
        trainer,
        X,
        y,
    ):

        tscv = TimeSeriesSplit(

            n_splits=self.n_splits

        )

        results = []

        print("\n" + "=" * 60)
        print("WALK FORWARD VALIDATION")
        print("=" * 60)

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

            mae = mean_absolute_error(
                y_test,
                pred,
            )

            rmse = math.sqrt(
                mean_squared_error(
                    y_test,
                    pred,
                )
            )

            r2 = r2_score(
                y_test,
                pred,
            )

            print(
                f"Fold {fold} | "
                f"MAE={mae:.6f} "
                f"RMSE={rmse:.6f} "
                f"R²={r2:.4f}"
            )

            results.append({

                "Fold": fold,

                "MAE": mae,

                "RMSE": rmse,

                "R2": r2,

            })

        print("=" * 60)

        return pd.DataFrame(results)