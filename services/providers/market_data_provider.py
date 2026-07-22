from __future__ import annotations

"""
BIST AI LAB
Market Data Provider v2.0
"""


import logging
import pandas as pd


logger = logging.getLogger(__name__)


class MarketDataProvider:


    def __init__(self):

        self.source = "Market"

    def get(self, symbol: str):

        return self.fetch(symbol)


    def fetch(self, symbol: str):

        symbol = symbol.upper()


        logger.info(
            "Market data request: %s",
            symbol
        )


        return self._demo_dataframe(symbol)



    def _demo_dataframe(self, symbol):


        if symbol != "ASELS":

            return pd.DataFrame()



        data = [

            {
                "Date":"2026-07-22",
                "Open":243.0,
                "High":247.0,
                "Low":242.5,
                "Close":245.5,
                "Volume":12500000
            },

            {
                "Date":"2026-07-21",
                "Open":240.0,
                "High":244.0,
                "Low":239.5,
                "Close":242.8,
                "Volume":11800000
            },

            {
                "Date":"2026-07-20",
                "Open":237.0,
                "High":241.0,
                "Low":236.5,
                "Close":239.4,
                "Volume":10200000
            }

        ]


        df = pd.DataFrame(data)


        df["Date"] = pd.to_datetime(
            df["Date"]
        )


        df = df.sort_values(
            "Date"
        )


        return df.reset_index(
            drop=True
        )



market_data_provider = MarketDataProvider()


__all__ = [
    "MarketDataProvider",
    "market_data_provider",
]