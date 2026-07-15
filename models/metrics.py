"""
Metrics
BIST AI LAB v3
"""

from __future__ import annotations

import math

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


class Metrics:

    @staticmethod
    def regression(
        y_true,
        y_pred,
    ):

        mae = mean_absolute_error(
            y_true,
            y_pred,
        )

        mse = mean_squared_error(
            y_true,
            y_pred,
        )

        rmse = math.sqrt(mse)

        r2 = r2_score(
            y_true,
            y_pred,
        )

        return {

            "MAE": round(mae, 6),

            "RMSE": round(rmse, 6),

            "R2": round(r2, 6),

        }