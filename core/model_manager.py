
"""
Model Manager
BIST AI LAB v5
"""

from __future__ import annotations

from core.model_bundle import ModelBundle


class ModelManager:

    def __init__(self):
        self.bundle = ModelBundle()

    def save_classifier(self, model, features, version="v5"):
        self.bundle.save(
            model=model,
            features=features,
            version=version,
        )

    def load_classifier(self):
        return self.bundle.load()

    def load_bundle(self):
        return self.bundle.load_bundle()

    def get_features(self):
        return self.bundle.features()

    def get_version(self):
        return self.bundle.version_name()
