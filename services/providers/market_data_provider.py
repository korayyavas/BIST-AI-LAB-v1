from __future__ import annotations

"""
BIST AI LAB
Market Data Provider v3.0
Real Market Data Engine
"""


import logging

import pandas as pd
import yfinance as yf


logger = logging.getLogger(__name__)


class MarketDataProvider:


    def __init__(self):

        self.source = "Yahoo Finance"



    def get(
        self,
        symbol: str
    ):

        return self.fetch(symbol)



    def fetch(
        self,
        symbol: str
    ):


        symbol = symbol.upper()


        logger.info(
            "Market data request: %s",
            symbol
        )


        try:

            ticker = f"{symbol}.IS"


            df = yf.download(

                ticker,

                period="5y",

                interval="1d",

                auto_adjust=False,

                progress=False

            )


            if df is None or df.empty:

                raise ValueError(
                    "Yahoo Finance data empty"
                )



            # MultiIndex temizleme

            if isinstance(
                df.columns,
                pd.MultiIndex
            ):

                df.columns = [

                    c[0]

                    for c in df.columns

                ]



            df = df.reset_index()



            rename_map = {

                "Adj Close":
                "Adj_Close"

            }


            df.rename(

                columns=rename_map,

                inplace=True

            )



            required = [

                "Date",

                "Open",

                "High",

                "Low",

                "Close",

                "Volume"

            ]


            df = df[required]



            df = df.dropna()



            df = df.sort_values(

                "Date"

            )


            logger.info(

                "Market rows loaded: %s",

                len(df)

            )


            return df.reset_index(
                drop=True
            )



        except Exception as e:


            logger.error(

                "Market data failed %s: %s",

                symbol,

                e

            )


            return pd.DataFrame()



market_data_provider = MarketDataProvider()



__all__ = [

    "MarketDataProvider",

    "market_data_provider",

]