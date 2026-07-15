"""
Cache Manager
BIST AI LAB v3
"""

from __future__ import annotations

from datetime import datetime, timedelta


class Cache:

    def __init__(

        self,

        ttl_minutes: int = 30,

    ):

        self.ttl = timedelta(

            minutes=ttl_minutes,

        )

        self.storage = {}

    # ==================================================

    def set(

        self,

        key: str,

        value,

    ):

        self.storage[key] = {

            "value": value,

            "time": datetime.now(),

        }

    # ==================================================

    def get(

        self,

        key: str,

    ):

        item = self.storage.get(key)

        if item is None:

            return None

        if datetime.now() - item["time"] > self.ttl:

            self.storage.pop(key)

            return None

        return item["value"]

    # ==================================================

    def exists(

        self,

        key: str,

    ) -> bool:

        return self.get(key) is not None

    # ==================================================

    def delete(

        self,

        key: str,

    ):

        self.storage.pop(

            key,

            None,

        )

    # ==================================================

    def clear(self):

        self.storage.clear()

    # ==================================================

    def size(self) -> int:

        return len(self.storage)