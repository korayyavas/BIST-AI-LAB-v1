"""
History Manager
BIST AI LAB v3
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime


class History:

    def __init__(self):

        self.file = Path("storage/history.json")

        self.file.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        if not self.file.exists():

            self.file.write_text(

                "[]",

                encoding="utf-8",

            )

    # ==================================================

    def add(

        self,

        ticker: str,

        prediction: dict,

    ):

        history = self.load()

        history.append(

            {

                "date": datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                ),

                "ticker": ticker,

                "prediction": prediction,

            }

        )

        with open(

            self.file,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                history,

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

    # ==================================================

    def last(

        self,

        count: int = 10,

    ):

        history = self.load()

        return history[-count:]

    # ==================================================

    def clear(self):

        self.file.write_text(

            "[]",

            encoding="utf-8",

        )