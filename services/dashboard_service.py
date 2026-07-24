"""
BIST AI LAB
Intelligence Dashboard Service v2.3
"""

from datetime import datetime
import logging


from services.prediction_service import PredictionService
from services.prediction_adapter import prediction_adapter

from services.technical_service import technical_service

from services.news_service import (
    news_dashboard,
)

from services.kap_service import (
    kap_dashboard,
)

from services.research_service import (
    research_dashboard,
)

from services.consensus_service import (
    calculate_consensus,
)


from services.providers.market_data_provider import (
    market_data_provider,
)



logger = logging.getLogger(__name__)




class DashboardService:


    def __init__(self):

        self.prediction_service = PredictionService()



    # ========================================================
    # SCORE EXTRACTORS
    # ========================================================


    def extract_news_score(self, data):

        return data.get(
            "statistics",
            {}
        ).get(
            "average_score",
            50
        )



    def extract_kap_score(self, data):

        return data.get(
            "statistics",
            {}
        ).get(
            "average_score",
            50
        )



    def extract_research_score(self, data):

        return data.get(
            "consensus",
            {}
        ).get(
            "score",
            50
        )




    # ========================================================
    # MARKET DATA
    # ========================================================


    def build_market_data(
        self,
        symbol
    ):


        market = {


            "symbol":

                symbol,


            "price":

                None,


            "change":

                0,


            "change_percent":

                0,


            "volume":

                0,


            "ohlcv":

                []

        }



        try:


            df = market_data_provider.get(

                symbol

            )



            if df.empty:

                return market



            latest = df.iloc[-1]


            previous = df.iloc[-2]



            close = float(

                latest["Close"]

            )



            prev_close = float(

                previous["Close"]

            )



            change = close - prev_close



            market.update({

                "price":

                    round(

                        close,

                        2

                    ),


                "change":

                    round(

                        change,

                        2

                    ),


                "change_percent":

                    round(

                        (

                            change /

                            prev_close

                        ) * 100,

                        2

                    )

                    if prev_close

                    else 0,


                "volume":

                    int(

                        latest["Volume"]

                    )

            })




            candles = []



            for _, row in df.tail(250).iterrows():


                candles.append({


                    "date":

                        str(

                            row["Date"]

                        ),



                    "open":

                        float(

                            row["Open"]

                        ),



                    "high":

                        float(

                            row["High"]

                        ),



                    "low":

                        float(

                            row["Low"]

                        ),



                    "close":

                        float(

                            row["Close"]

                        ),



                    "volume":

                        int(

                            row["Volume"]

                        )

                })



            market["ohlcv"] = candles



        except Exception as e:


            logger.exception(

                "Market data error %s",

                e

            )



        return market






    # ========================================================
    # BUILD DASHBOARD
    # ========================================================


    def build(
        self,
        symbol: str,
    ):


        symbol = symbol.upper()



        logger.info(

            "Building dashboard for %s",

            symbol

        )



        # ----------------------------------------------------
        # DATA
        # ----------------------------------------------------


        news = news_dashboard(

            symbol

        )


        kap = kap_dashboard(

            symbol

        )


        research = research_dashboard(

            symbol

        )


        technical = technical_service.analyze(

            symbol

        )



        market = self.build_market_data(

            symbol

        )




        # ----------------------------------------------------
        # ML
        # ----------------------------------------------------


        prediction = prediction_adapter.predict(

            symbol

        )



        ml_score = prediction.get(

            "top_score",

            50

        )



        confidence = prediction.get(

            "confidence",

            50

        )



        decision = prediction.get(

            "signal",

            "HOLD"

        )




        # ----------------------------------------------------
        # COMPONENT SCORES
        # ----------------------------------------------------


        components = {


            "ml":

                float(

                    ml_score

                    or 50

                ),



           "technical":
            float(
                technical.get(
                    "score",
                    50
                )
            ),


            "news":

                float(

                    self.extract_news_score(

                        news

                    )

                    or 50

                ),



            "research":

                float(

                    self.extract_research_score(

                        research

                    )

                    or 50

                ),



            "kap":

                float(

                    self.extract_kap_score(

                        kap

                    )

                    or 50

                ),

        }




        # ----------------------------------------------------
        # CONSENSUS
        # ----------------------------------------------------


        consensus = calculate_consensus(

            symbol,

            components

        )



        ai_score = consensus.get(

            "score",

            sum(

                components.values()

            )

            /

            len(

                components

            )

        )




        confidence = float(

            confidence

            or

            consensus.get(

                "confidence",

                50

            )

        )





        # ----------------------------------------------------
        # INTELLIGENCE
        # ----------------------------------------------------


        intelligence = {


            "ai_score":

                round(

                    ai_score,

                    2

                ),



            "decision":

                decision,



            "confidence":

                round(

                    confidence,

                    2

                ),



            "ml_score":

                components["ml"],



            "technical_score":

                components["technical"],



            "news_score":

                components["news"],



            "research_score":

                components["research"],



            "kap_score":

                components["kap"],



            "strengths":

                [],



            "weaknesses":

                [],



            "explanations":

                [],

        }






        # ----------------------------------------------------
        # RESPONSE
        # ----------------------------------------------------


        return {


            "symbol":

                symbol,



            "price":

                technical.get(

                    "price"

                ),



            "market":

                market,



            "trend":

                technical.get(

                    "trend",

                    "UNKNOWN"

                ),



            "news":

                news,



            "kap":

                kap,



            "research":

                research,



            "technical":

                technical,



            "prediction":

                prediction,



            "consensus":

                consensus,



            "intelligence":

                intelligence,



            "version":

                {

                    "version":

                    "v10.1"

                },



            "modules":

                {

                    "ml": True,

                    "news": True,

                    "kap": True,

                    "research": True,

                    "technical": True,

                    "market": True

                },



            "loadedAt":

                datetime.utcnow().isoformat(),



        }







# ============================================================
# SINGLETON
# ============================================================


dashboard_service = DashboardService()




def get_dashboard(symbol: str):


    return dashboard_service.build(

        symbol

    )




def dashboard_health():


    return {


        "service":

            "Dashboard Intelligence",



        "status":

            "ok"

    }




__all__ = [

    "DashboardService",

    "dashboard_service",

    "get_dashboard",

    "dashboard_health",

]