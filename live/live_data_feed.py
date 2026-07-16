
"""
Live Data Feed
BIST AI LAB v5
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime


class LiveDataFeed(ABC):

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def subscribe(self, symbol: str):
        ...

    @abstractmethod
    def latest(self, symbol: str):
        ...

    @abstractmethod
    def disconnect(self):
        ...


class MockLiveDataFeed(LiveDataFeed):

    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def subscribe(self, symbol: str):
        return True

    def latest(self, symbol: str):
        return {
            "symbol": symbol,
            "timestamp": datetime.now().isoformat(),
            "price": None,
            "volume": None,
        }

    def disconnect(self):
        self.connected = False
