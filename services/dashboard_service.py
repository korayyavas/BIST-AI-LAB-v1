"""
BIST AI LAB
Intelligence Dashboard Service v2.2
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

            65,



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
        # INTELLIGENCE OBJECT
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

                "v10.0"

            },



            "modules":

            {

                "ml":

                True,

                "news":

                True,

                "kap":

                True,

                "research":

                True,

                "technical":

                True

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