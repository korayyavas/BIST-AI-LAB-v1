"""
KAP Service
BIST AI LAB v7
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KapEvent:

    title: str

    event_type: str

    score: float


class KapService:

    def get_announcements(self, symbol: str):

        return [

            KapEvent(

                title=f"{symbol} KAP Service Ready",

                event_type="INFO",

                score=50,

            )

        ]

    # ===========================================
    # Backward Compatibility
    # ===========================================

    def get_events(self, symbol: str):

        return self.get_announcements(symbol)