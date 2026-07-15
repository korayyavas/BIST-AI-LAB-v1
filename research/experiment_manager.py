"""
Experiment Manager
BIST AI LAB v3
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime


class ExperimentManager:

    def __init__(self):

        self.folder = Path("research")

        self.folder.mkdir(
            exist_ok=True,
        )

        self.file = self.folder / "experiments.json"

        if not self.file.exists():

            self.file.write_text(
                "[]",
                encoding="utf-8",
            )

    # ==================================================

    def save(

        self,

        model_name: str,

        metrics: dict,

        feature_count: int,

    ):

        experiments = self.load()

        experiments.append(

            {

                "date": datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                ),

                "model": model_name,

                "features": feature_count,

                "metrics": metrics,

            }

        )

        with open(

            self.file,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                experiments,

                f,

                indent=4,

                ensure_ascii=False,

            )

    # ==================================================

    def load(self):

        with open(

            self.file,

            "r",

            encoding="utf-8",

        ) as f:

            return json.load(f)