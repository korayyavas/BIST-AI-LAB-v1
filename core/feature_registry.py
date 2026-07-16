"""
Feature Registry
BIST AI LAB v5
"""

from __future__ import annotations

from core.feature_store import FeatureStore


class FeatureRegistry:

    def __init__(self):
        self.store = FeatureStore()

    def register(self, features):
        self.store.save(list(features))

    def features(self):
        return self.store.load()

    def apply(self, X):
        return self.store.transform(X)

    def exists(self):
        return self.store.exists()
