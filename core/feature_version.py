
"""
Feature Version
BIST AI LAB v5
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime


class FeatureVersion:

    def __init__(self, path: str = "models/feature_version.json"):
        self.path = Path(path)

    def save(self, version: str, features: list[str]):

        self.path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "version": version,
            "created_at": datetime.now().isoformat(),
            "feature_count": len(features),
            "features": features,
        }

        self.path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8",
        )

    def load(self):

        if not self.path.exists():
            raise FileNotFoundError(
                f"Version dosyası bulunamadı: {self.path}"
            )

        return json.loads(
            self.path.read_text(encoding="utf-8")
        )

    def current_version(self):

        return self.load()["version"]
