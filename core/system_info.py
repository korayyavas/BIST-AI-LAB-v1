
"""
System Information
BIST AI LAB v6
"""

from __future__ import annotations

import platform
import sys
from datetime import datetime

from core.version import (
    APP_NAME,
    VERSION,
    CODENAME,
    STAGE,
    BUILD,
)


class SystemInfo:

    @staticmethod
    def info():

        return {
            "app": APP_NAME,
            "version": VERSION,
            "codename": CODENAME,
            "stage": STAGE,
            "build": BUILD,
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "started_at": datetime.now().isoformat(),
        }
