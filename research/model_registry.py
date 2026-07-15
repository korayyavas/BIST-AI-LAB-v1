"""
Model Registry
BIST AI LAB v3
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime


class ModelRegistry:

    def __init__(self):

        self.file = Path(
            "research/model_registry.json"
        )

        if not self.file.exists():

            self.file.parent.mkdir(
                exist_ok=True
            )

            self.file.write_text(
                "[]",
                encoding="utf-8",
            )

    # ==================================================

    def register(

        self,

        model_name: str,

        version: str,

        metrics: dict,

    ):

        registry = self.load()

        registry.append({

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "model": model_name,

            "version": version,

            "metrics": metrics,

        })

        with open(

            self.file,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                registry,

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