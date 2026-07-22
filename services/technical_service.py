from __future__ import annotations

"""
BIST AI LAB
Technical Analysis Service v1.1
"""

import logging

from typing import Dict, List

from services.providers.market_data_provider import (
    market_data_provider,
)


logger = logging.getLogger(__name__)


class TechnicalService:


    def __init__(self):

        self.provider = market_data_provider



    def analyze(

        self,

        symbol: str,

    ) -> Dict:


        symbol = symbol.upper()


        logger.info(

            "Technical analysis: %s",

            symbol

        )


        data = self.provider.fetch(symbol)
        print("MARKET DATA COLUMNS:", data.columns.tolist())
        print(data.head())

        if data is None:

            return {

                "symbol": symbol,

                "status": "NO_DATA"

            }


        # =========================================
        # DATAFRAME SUPPORT
        # =========================================

        if hasattr(data, "columns"):

            if data.empty:
                return {
                    "symbol": symbol,
                    "status": "NO_DATA"
                }


    # kolon isimlerini normalize et
            data.columns = [
                str(c).lower()
                for c in data.columns
            ]


            close_column = "close"

            if close_column not in data.columns:

                return {
                    "symbol": symbol,
                    "status": "INVALID_DATA",
                    "columns": data.columns.tolist()
                }


            closes = (
                data[close_column]
                .astype(float)
                .tolist()
            )


            current = float(
                data[close_column].iloc[-1]
            )


        # =========================================
        # OLD LIST SUPPORT
        # =========================================

        else:

            if len(data) == 0:

                return {

                    "symbol": symbol,

                    "status": "NO_DATA"

                }


            closes = [

                float(x["close"])

                for x in data

            ]


            current = float(

                data[-1]["close"]

            )



        if len(closes) < 2:

            previous = current

        else:

            previous = closes[-2]



        change = (

            (current - previous)

            /

            previous

        ) * 100



        trend = (

            "BULLISH"

            if change > 0

            else

            "BEARISH"

        )



        score = 50


        if change > 0:

            score += 15

        else:

            score -= 15



        return {


            "symbol":

            symbol,


            "price":

            current,


            "change_percent":

            round(

                change,

                2

            ),


            "trend":

            trend,


            "rsi":

            self._fake_rsi(closes),


            "macd":

            (

                "POSITIVE"

                if change > 0

                else

                "NEGATIVE"

            ),


            "score":

            max(

                0,

                min(

                    100,

                    score

                )

            )

        }



    def _fake_rsi(

        self,

        closes: List[float]

    ) -> float:


        if len(closes) < 2:

            return 50


        return 60.0



technical_service = TechnicalService()



__all__ = [

    "TechnicalService",

    "technical_service",

]