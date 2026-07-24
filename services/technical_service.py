from __future__ import annotations

"""
BIST AI LAB
Technical Analysis Service v1.2

Real Technical Intelligence Engine
"""

import logging

from typing import Dict, List

import pandas as pd


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



        if data is None or data.empty:


            return {


                "symbol":

                    symbol,


                "status":

                    "NO_DATA"


            }





        data.columns = [

            str(c).lower()

            for c in data.columns

        ]



        if "close" not in data.columns:


            return {


                "symbol":

                    symbol,


                "status":

                    "INVALID_DATA"


            }




        closes = (

            data["close"]

            .astype(float)

        )



        current = float(

            closes.iloc[-1]

        )






        # ====================================================
        # CHANGE
        # ====================================================


        previous = float(

            closes.iloc[-2]

        ) if len(closes) > 1 else current



        change_percent = (

            (

                current - previous

            )

            /

            previous

            *

            100

        ) if previous else 0







        # ====================================================
        # RSI 14
        # ====================================================


        rsi = self.calculate_rsi(

            closes

        )







        # ====================================================
        # MOVING AVERAGES
        # ====================================================


        ma20 = float(

            closes.rolling(

                20

            )

            .mean()

            .iloc[-1]

        )



        ma50 = float(

            closes.rolling(

                50

            )

            .mean()

            .iloc[-1]

        )



        ma_trend = (


            "ABOVE_MA50"

            if current > ma50

            else

            "BELOW_MA50"

        )








        # ====================================================
        # MACD
        # ====================================================


        macd = self.calculate_macd(

            closes

        )







        # ====================================================
        # SUPPORT / RESISTANCE
        # ====================================================


        support = float(

            closes.tail(60)

            .min()

        )



        resistance = float(

            closes.tail(60)

            .max()

        )








        # ====================================================
        # TREND
        # ====================================================


        if current > ma20 and current > ma50:


            trend = "BULLISH"


        elif current < ma20 and current < ma50:


            trend = "BEARISH"


        else:


            trend = "NEUTRAL"









        # ====================================================
        # SCORE
        # ====================================================


        score = 50



        if rsi < 30:

            score += 15


        elif rsi > 70:

            score -= 10



        if current > ma50:

            score += 10

        else:

            score -= 10




        if macd["trend"] == "POSITIVE":

            score += 10

        else:

            score -= 10




        score = max(

            0,

            min(

                100,

                score

            )

        )









        return {



            "symbol":

                symbol,



            "price":

                round(

                    current,

                    2

                ),



            "change_percent":

                round(

                    change_percent,

                    2

                ),



            "trend":

                trend,



            "rsi":

                round(

                    rsi,

                    2

                ),



            "macd":

                macd,



            "moving_average":

                {


                    "ma20":

                        round(

                            ma20,

                            2

                        ),



                    "ma50":

                        round(

                            ma50,

                            2

                        ),



                    "trend":

                        ma_trend

                },



            "support":

                round(

                    support,

                    2

                ),



            "resistance":

                round(

                    resistance,

                    2

                ),



            "score":

                score



        }








    # ========================================================
    # RSI
    # ========================================================


    def calculate_rsi(

        self,

        closes,

        period=14

    ):



        delta = closes.diff()



        gain = delta.clip(

            lower=0

        )



        loss = -delta.clip(

            upper=0

        )



        avg_gain = gain.rolling(

            period

        ).mean()



        avg_loss = loss.rolling(

            period

        ).mean()



        rs = avg_gain / avg_loss



        rsi = 100 - (

            100 /

            (

                1 + rs

            )

        )



        value = rsi.iloc[-1]



        if pd.isna(value):

            return 50



        return float(value)







    # ========================================================
    # MACD
    # ========================================================


    def calculate_macd(

        self,

        closes

    ):



        ema12 = closes.ewm(

            span=12,

            adjust=False

        ).mean()



        ema26 = closes.ewm(

            span=26,

            adjust=False

        ).mean()



        macd_line = ema12 - ema26



        signal = macd_line.ewm(

            span=9,

            adjust=False

        ).mean()



        histogram = (

            macd_line.iloc[-1]

            -

            signal.iloc[-1]

        )



        return {


            "value":

                round(

                    float(

                        macd_line.iloc[-1]

                    ),

                    3

                ),



            "signal":

                round(

                    float(

                        signal.iloc[-1]

                    ),

                    3

                ),



            "histogram":

                round(

                    float(

                        histogram

                    ),

                    3

                ),



            "trend":

                (

                    "POSITIVE"

                    if histogram > 0

                    else

                    "NEGATIVE"

                )


        }





technical_service = TechnicalService()





__all__ = [

    "TechnicalService",

    "technical_service",

]