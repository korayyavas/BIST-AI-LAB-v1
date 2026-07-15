"""
Model Store
BIST AI LAB v3
"""

from __future__ import annotations

from pathlib import Path
import shutil


class ModelStore:

    def __init__(self):

        self.folder = Path("storage/models")

        self.folder.mkdir(

            parents=True,

            exist_ok=True,

        )

    # ==================================================

    def save_version(

        self,

        source_model,

        version: str,

    ):

        destination = self.folder / f"{version}.joblib"

        shutil.copy2(

            source_model,

            destination,

        )

        return destination

    # ==================================================

    def list_models(self):

        return sorted(

            [

                x.name

                for x in self.folder.glob("*.joblib")

            ]

        )

    # ==================================================

    def latest(self):

        models = sorted(

            self.folder.glob("*.joblib"),

            key=lambda x: x.stat().st_mtime,

            reverse=True,

        )

        if not models:

            return None

        return models[0]

    # ==================================================

    def delete(

        self,

        version: str,

    ):

        file = self.folder / f"{version}.joblib"

        if file.exists():

            file.unlink()