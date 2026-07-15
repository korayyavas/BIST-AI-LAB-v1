"""
Model Manager
BIST AI LAB v3
"""

from __future__ import annotations

from pathlib import Path

import joblib

from config.settings import (
    MODEL_PATH,
    MODEL_FILE,
)


class ModelManager:

    def __init__(self):

        self.model_path = Path(
            MODEL_PATH
        )

        self.model_path.mkdir(

            parents=True,

            exist_ok=True,

        )

        self.file = (
            self.model_path
            / MODEL_FILE
        )

        self.model = None

    # ==================================================

    def save(
        self,
        model,
    ):

        joblib.dump(
            model,
            self.file,
        )

        self.model = model

    # ==================================================

    def load(self):

        if not self.file.exists():

            raise FileNotFoundError(

                f"Model not found: {self.file}"

            )

        self.model = joblib.load(
            self.file
        )

        return self.model

    # ==================================================

    def predict(
        self,
        X,
    ):

        if self.model is None:

            self.load()

        return self.model.predict(X)

    # ==================================================

    def exists(self):

        return self.file.exists()

    # ==================================================

    def delete(self):

        if self.file.exists():

            self.file.unlink()

            self.model = None