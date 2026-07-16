
"""
Model Bundle
BIST AI LAB v5
"""

from __future__ import annotations

import joblib

from core.feature_registry import FeatureRegistry
from core.feature_version import FeatureVersion


class ModelBundle:

    def __init__(self, path: str = "models/model_bundle.joblib"):
        self.path = path
        self.registry = FeatureRegistry()
        self.version = FeatureVersion()

    def save(self, model, features, version="v5"):

        bundle = {
            "model": model,
            "features": list(features),
            "version": version,
        }

        joblib.dump(bundle, self.path)

        self.registry.register(features)
        self.version.save(version, list(features))

    def load(self):

        bundle = joblib.load(self.path)

        return bundle["model"]

    def load_bundle(self):

        return joblib.load(self.path)

    def features(self):

        return self.load_bundle()["features"]

    def version_name(self):

        return self.load_bundle()["version"]
