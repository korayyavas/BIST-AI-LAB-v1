
"""
Startup
BIST AI LAB v6
"""

from __future__ import annotations

from core.logging_config import configure_logging
from core.system_info import SystemInfo
from core.service_container import ServiceContainer


class Startup:

    def __init__(self):
        self.logger = configure_logging()
        self.container = ServiceContainer()

    def boot(self):

        info = SystemInfo.info()

        self.logger.info(
            "%s %s (%s)",
            info["app"],
            info["version"],
            info["stage"],
        )

        return {
            "system": info,
            "container": self.container,
            "success": True,
        }
