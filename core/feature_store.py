"""
Feature Store
BIST AI LAB v5
"""

from __future__ import annotations

import json
from pathlib import Path


class FeatureStore:

    def __init__(self, path: str = "models/feature_store.json"):
        self.path = Path(path)

    def save(self, features: list[str]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(features, indent=2),
            encoding="utf-8",
        )

    def load(self) -> list[str]:
        if not self.path.exists():
            raise FileNotFoundError(
                f"Feature store bulunamadı: {self.path}"
            )
        return json.loads(
            self.path.read_text(encoding="utf-8")
        )

    def transform(self, X):
        features = self.load()
        missing = [f for f in features if f not in X.columns]
        if missing:
            raise ValueError(
                f"Eksik feature'lar: {missing}"
            )
        return X[features].copy()

    def exists(self) -> bool:
        return self.path.exists()
