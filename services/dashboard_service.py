"""
BIST AI LAB
Intelligence Dashboard Service v2.1
"""

from services.prediction_service import PredictionService
import logging

from datetime import datetime
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
    # SCORE NORMALIZER
    # ========================================================


    def extract_news_score(
        self,
        data
    ):

        return data.get(
            "statistics",
            {}
        ).get(
            "average_score",
            50
        )



    def extract_kap_score(
        self,
        data
    ):

        return data.get(
            "statistics",
            {}
        ).get(
            "average_score",
            50
        )



    def extract_research_score(
        self,
        data
    ):

        return data.get(
            "consensus",
            {}
        ).get(
            "score",
            50
        )



    # ========================================================
    # MAIN DASHBOARD
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
        # DATA SOURCES
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
        # COMPONENT SCORES
        # ----------------------------------------------------


        prediction = prediction_adapter.predict(
            symbol
        )


        ml_score = 50


        try:

            prediction = self.prediction_service.predict(
                features=None,
                current_price=None
            )


            ml_score = prediction.get(
                "top_score",
                50
            )


        except Exception as e:

            logger.warning(
                "Prediction unavailable: %s",
                e
            )


        components = {

            "news":
            self.extract_news_score(news),

            "kap":
            self.extract_kap_score(kap),

            "research":
            self.extract_research_score(research),

            "technical":
            65,

            "ml":
            ml_score,

        }



        consensus = calculate_consensus(

            symbol,

            components

        )



        # ----------------------------------------------------
        # FINAL RESPONSE
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



            "consensus":

            consensus,



            "technical":

            technical,



            "prediction":

            {

                "status":

                "waiting"

            },



            "generated_at":

            datetime.utcnow().isoformat(),

        }



# ============================================================
# SINGLETON
# ============================================================


dashboard_service = DashboardService()



# ============================================================
# PUBLIC API
# ============================================================


def get_dashboard(

    symbol: str,

):


    return dashboard_service.build(

        symbol

    )



def dashboard_health():


    return {


        "service":

        "Dashboard Intelligence",


        "status":

        "ok",

    }



__all__ = [

    "DashboardService",

    "dashboard_service",

    "get_dashboard",

    "dashboard_health",

]