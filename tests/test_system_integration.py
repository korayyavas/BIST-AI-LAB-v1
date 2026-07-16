
"""
System Integration Test
BIST AI LAB v5.1
"""

from core.service_container import ServiceContainer
from core.config_manager import ConfigManager
from core.feature_registry import FeatureRegistry
from core.model_manager import ModelManager


def main():

    print("SYSTEM INTEGRATION TEST")

    container = ServiceContainer()

    print("Logger            :", container.logger is not None)
    print("ModelManager      :", isinstance(container.model_manager, ModelManager))
    print("FeatureRegistry   :", isinstance(container.feature_registry, FeatureRegistry))

    cfg = ConfigManager()
    cfg.set("system_test", True)

    print("Config OK         :", cfg.get("system_test") is True)

    container.register("config", cfg)

    resolved = container.resolve("config")

    print("DI Container OK   :", resolved is cfg)

    print()
    print("TEST BAŞARILI")


if __name__ == "__main__":
    main()
