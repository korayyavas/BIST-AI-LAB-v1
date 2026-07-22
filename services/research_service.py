from __future__ import annotations

"""
services/research_service.py

BIST AI LAB
Research Intelligence Service v1.0

"""



import logging

from dataclasses import dataclass, asdict

from datetime import datetime

from typing import List
from services.providers.research_provider import research_provider

logger = logging.getLogger(__name__)


# ============================================================
# DATA MODEL
# ============================================================


@dataclass(slots=True)
class ResearchItem:

    symbol: str

    source: str

    analyst: str = ""

    recommendation: str = "UNKNOWN"

    target_price: float = 0

    current_price: float = 0

    upside: float = 0

    risk: str = "UNKNOWN"

    score: float = 0

    summary: str = ""

    published_at: str = ""

    url: str = ""

    ai_comment: str = ""



# ============================================================
# ANALYZER
# ============================================================


class ResearchAnalyzer:


    def analyze(

        self,

        item: ResearchItem,

    ) -> ResearchItem:


        if item.current_price > 0 and item.target_price > 0:

            item.upside = round(

                (

                    (

                        item.target_price

                        -

                        item.current_price

                    )

                    /

                    item.current_price

                )

                *

                100,

                2,

            )


        recommendation = (

            item.recommendation.upper()

        )


        if recommendation == "BUY":

            item.score = 80

            item.risk = "LOW"


        elif recommendation == "HOLD":

            item.score = 55

            item.risk = "MEDIUM"


        elif recommendation == "SELL":

            item.score = 25

            item.risk = "HIGH"


        else:

            item.score = 50

            item.risk = "UNKNOWN"



        return item



# ============================================================
# SERVICE
# ============================================================


class ResearchService:


    def __init__(self):

        self.analyzer = ResearchAnalyzer()



    def fetch(

        self,

        symbol: str,

    ) -> List[ResearchItem]:


        """
        Araştırma raporu sağlayıcı adaptörü.
        PDF / aracı kurum raporları için hazır katman.
        """


        logger.info(

            "Searching research reports for %s",

            symbol

        )


        return []



    def analyze(

        self,

        items: List[ResearchItem],

    ):


        return [

            self.analyzer.analyze(item)

            for item in items

        ]



    def consensus(

        self,

        items: List[ResearchItem],

    ):


        buy = len(

            [

                x

                for x in items

                if x.recommendation.upper()

                == "BUY"

            ]

        )


        hold = len(

            [

                x

                for x in items

                if x.recommendation.upper()

                == "HOLD"

            ]

        )


        sell = len(

            [

                x

                for x in items

                if x.recommendation.upper()

                == "SELL"

            ]

        )


        average = round(

            sum(

                x.score

                for x in items

            )

            /

            len(items),

            2

        ) if items else 0



        return {


            "buy":

            buy,


            "hold":

            hold,


            "sell":

            sell,


            "average_score":

            average,

        }



    def dashboard(

        self,

        symbol: str,

    ):


        items = self.fetch(

            symbol

        )


        items = self.analyze(

            items

        )


        return {


            "symbol":

            symbol,


            "count":

            len(items),


            "items":

            [

                asdict(item)

                for item in items

            ],


            "consensus":

            self.consensus(

                items

            ),


            "generated_at":

            datetime.utcnow().isoformat(),

        }



# ============================================================
# SINGLETON
# ============================================================


research_service = ResearchService()



# ============================================================
# PUBLIC FUNCTIONS
# ============================================================


def get_research(

    symbol: str,

):


    return research_service.fetch(

        symbol

    )



def research_dashboard(

    symbol: str,

):


    return research_service.dashboard(

        symbol

    )



def research_health():


    return {


        "service":

        "Research Intelligence",


        "status":

        "ok",

    }



__all__ = [

    "ResearchItem",

    "ResearchService",

    "research_service",

    "get_research",

    "research_dashboard",

    "research_health",

]