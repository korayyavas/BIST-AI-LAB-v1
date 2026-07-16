
"""
Feature Schema
BIST AI LAB v5
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FeatureSchema:

    version: str = "v5"

    features: list[str] = field(default_factory=list)

    target: str = "TARGET"

    future_return: str = "FUTURE_RETURN"

    def add(self, feature: str):

        if feature not in self.features:
            self.features.append(feature)

    def extend(self, features):

        for feature in features:
            self.add(feature)

    def validate(self, columns):

        missing = [
            feature
            for feature in self.features
            if feature not in columns
        ]

        if missing:
            raise ValueError(
                f"Eksik feature'lar: {missing}"
            )

        return True

    def to_dict(self):

        return {
            "version": self.version,
            "features": self.features,
            "target": self.target,
            "future_return": self.future_return,
        }
