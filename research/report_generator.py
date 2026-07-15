"""
Research Report Generator
BIST AI LAB v3
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime

import pandas as pd


class ReportGenerator:

    def __init__(self):

        self.folder = Path("reports")

        self.folder.mkdir(
            exist_ok=True,
        )

    # ==================================================

    def save_metrics(
        self,
        metrics: dict,
        filename: str = "metrics.csv",
    ):

        df = pd.DataFrame([metrics])

        path = self.folder / filename

        df.to_csv(
            path,
            index=False,
        )

        return path

    # ==================================================

    def save_features(
        self,
        importance: pd.DataFrame,
        filename: str = "feature_importance.csv",
    ):

        path = self.folder / filename

        importance.to_csv(
            path,
            index=False,
        )

        return path

    # ==================================================

    def save_validation(
        self,
        validation: pd.DataFrame,
        filename: str = "validation.csv",
    ):

        path = self.folder / filename

        validation.to_csv(
            path,
            index=False,
        )

        return path

    # ==================================================

    def summary(
        self,
        metrics: dict,
        feature_count: int,
    ) -> str:

        text = f"""
BIST AI LAB v3 REPORT

Date: {datetime.now():%Y-%m-%d %H:%M:%S}

Features : {feature_count}

MAE  : {metrics['MAE']}
RMSE : {metrics['RMSE']}
R2   : {metrics['R2']}
"""

        path = self.folder / "summary.txt"

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(text)

        return str(path)