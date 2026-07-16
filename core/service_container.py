
"""
Service Container
BIST AI LAB v5.1
"""

from __future__ import annotations

from core.app_context import AppContext
from core.config_manager import ConfigManager


class ServiceContainer:

    def __init__(self):
        self.context = AppContext()
        self.config = ConfigManager()
        self._services = {}

    def register(self, name: str, service):
        self._services[name] = service
        return service

    def resolve(self, name: str):
        if name not in self._services:
            raise KeyError(f"Service not registered: {name}")
        return self._services[name]

    @property
    def logger(self):
        return self.context.get_logger()

    @property
    def model_manager(self):
        return self.context.get_model_manager()

    @property
    def feature_registry(self):
        return self.context.get_feature_registry()
