"""
Model Manager
BIST AI LAB v6
"""

from __future__ import annotations

from core.model_bundle import ModelBundle


class ModelManager:

    def __init__(self):

        self.classifier_bundle = ModelBundle("classifier")
        self.regressor_bundle = ModelBundle("regressor")

    # =====================================================
    # CLASSIFIER
    # =====================================================

    def save_classifier(self, model, features, version="v6"):

        self.classifier_bundle.save(
            model=model,
            features=features,
            version=version,
        )

    def load_classifier(self):

        return self.classifier_bundle.load()

    # =====================================================
    # REGRESSOR
    # =====================================================

    def save_regressor(self, model, features, version="v6"):

        self.regressor_bundle.save(
            model=model,
            features=features,
            version=version,
        )

    def load_regressor(self):

        return self.regressor_bundle.load()

    # =====================================================
    # BACKWARD COMPATIBILITY
    # =====================================================

    def save(self, model, features, version="v6"):

        return self.save_regressor(
            model=model,
            features=features,
            version=version,
        )

    def load(self):

        return self.load_regressor()

    # =====================================================

    def get_classifier_features(self):

        return self.classifier_bundle.features()

    def get_regressor_features(self):

        return self.regressor_bundle.features()

    def get_classifier_version(self):

        return self.classifier_bundle.version_name()

    def get_regressor_version(self):

        return self.regressor_bundle.version_name()

    # =====================================================
    # Legacy
    # =====================================================

    def get_features(self):

        return self.get_classifier_features()

    def get_version(self):

        return self.get_classifier_version()