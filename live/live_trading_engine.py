
"""
Live Trading Engine
BIST AI LAB v5
"""

from __future__ import annotations

from live.live_data_feed import LiveDataFeed
from broker.broker_adapter import BrokerAdapter
from services.prediction_service import PredictionService


class LiveTradingEngine:

    def __init__(
        self,
        feed: LiveDataFeed,
        broker: BrokerAdapter,
    ):
        self.feed = feed
        self.broker = broker
        self.predictor = PredictionService()

    def start(self, symbol: str):
        self.feed.connect()
        self.feed.subscribe(symbol)
        self.broker.connect()

    def process(self, symbol: str, df, features, atr):

        tick = self.feed.latest(symbol)

        signal = self.predictor.predict(
            df=df,
            features=features,
            atr=atr,
        )

        return {
            "tick": tick,
            "signal": signal,
        }

    def stop(self):
        self.feed.disconnect()
        self.broker.disconnect()
