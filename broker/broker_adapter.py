
"""
Broker Adapter
BIST AI LAB v5
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BrokerAdapter(ABC):

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def get_balance(self):
        ...

    @abstractmethod
    def get_positions(self):
        ...

    @abstractmethod
    def place_order(
        self,
        symbol:str,
        side:str,
        quantity:float,
        price:float|None=None,
    ):
        ...

    @abstractmethod
    def cancel_order(self, order_id):
        ...

    @abstractmethod
    def disconnect(self):
        ...
