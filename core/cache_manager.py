"""
Cache Manager
BIST AI LAB v8
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


class CacheManager:

    def __init__(self, folder="cache"):

        self.folder = Path(folder)

        self.folder.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _file(self, key):

        name = hashlib.md5(
            key.encode()
        ).hexdigest()

        return self.folder / f"{name}.json"

    def exists(self, key):

        return self._file(key).exists()

    def load(self, key):

        with open(
            self._file(key),
            encoding="utf-8",
        ) as f:

            return json.load(f)

    def save(self, key, value):

        with open(
            self._file(key),
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                value,
                f,
                ensure_ascii=False,
                indent=2,
            )

    def get(self, key, producer):

        if self.exists(key):

            return self.load(key)

        value = producer()

        self.save(
            key,
            value,
        )

        return value

    def clear(self):

        for file in self.folder.glob("*.json"):

            file.unlink()