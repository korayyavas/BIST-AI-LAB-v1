
"""
Application Context
BIST AI LAB v5.1
"""

from __future__ import annotations

from core.logging_config import configure_logging
from core.model_manager import ModelManager
from core.feature_registry import FeatureRegistry


class AppContext:

    def __init__(self):

        self.logger = configure_logging()

        self.model_manager = ModelManager()

        self.feature_registry = FeatureRegistry()

    def get_logger(self):
        return self.logger

    def get_model_manager(self):
        return self.model_manager

    def get_feature_registry(self):
        return self.feature_registry
