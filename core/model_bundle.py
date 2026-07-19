"""
Model Bundle
BIST AI LAB v6
"""

from __future__ import annotations

from pathlib import Path
import joblib

from core.feature_registry import FeatureRegistry
from core.feature_version import FeatureVersion


class ModelBundle:

    def __init__(self, model_type: str = "classifier"):

        self.model_type = model_type

        self.models_dir = Path("models")
        self.models_dir.mkdir(exist_ok=True)

        self.path = self.models_dir / f"{model_type}_bundle.joblib"

        self.registry = FeatureRegistry()
        self.version = FeatureVersion()

    def save(self, model, features, version="v6"):

        bundle = {
            "model": model,
            "features": list(features),
            "version": version,
            "type": self.model_type,
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