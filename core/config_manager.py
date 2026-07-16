
"""
Configuration Manager
BIST AI LAB v5.1
"""

from __future__ import annotations

import json
from pathlib import Path


class ConfigManager:

    def __init__(self, path: str = "config/runtime_config.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, config: dict):
        self.path.write_text(
            json.dumps(config, indent=2),
            encoding="utf-8",
        )

    def get(self, key, default=None):
        return self.load().get(key, default)

    def set(self, key, value):
        cfg = self.load()
        cfg[key] = value
        self.save(cfg)
        return value
