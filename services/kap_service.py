from __future__ import annotations
"""
services/kap_service.py

BIST AI LAB
KAP Intelligence Service v1.0

"""



import logging

from dataclasses import dataclass, asdict, field
from services.providers.kap_provider import kap_provider
from datetime import datetime

from typing import Any, Dict, List


logger = logging.getLogger(__name__)


# ============================================================
# DATA MODEL
# ============================================================


@dataclass(slots=True)
class KAPItem:

    symbol: str

    title: str

    summary: str = ""

    category: str = "OTHER"

    importance: int = 0

    market_effect: str = "UNKNOWN"

    score: float = 0

    published_at: str = ""

    url: str = ""

    ai_comment: str = ""



# ============================================================
# KAP ANALYZER
# ============================================================


class KAPAnalyzer:


    POSITIVE_WORDS = [

        "sözleşme",

        "ihale",

        "sipariş",

        "anlaşma",

        "yatırım",

        "kapasite",

        "kar",

        "temettü",

        "geri alım",

    ]


    NEGATIVE_WORDS = [

        "zarar",

        "dava",

        "ceza",

        "iptal",

        "risk",

        "borç",

        "gecikme",

    ]



    def analyze(

        self,

        item: KAPItem,

    ) -> KAPItem:


        text = (

            item.title

            +

            " "

            +

            item.summary

        ).lower()



        positive = sum(

            1

            for word in self.POSITIVE_WORDS

            if word in text

        )


        negative = sum(

            1

            for word in self.NEGATIVE_WORDS

            if word in text

        )



        if positive > negative:

            item.market_effect = "POSITIVE"

            item.score = 75 + positive * 5



        elif negative > positive:

            item.market_effect = "NEGATIVE"

            item.score = 30 - negative * 5



        else:

            item.market_effect = "NEUTRAL"

            item.score = 50



        item.score = max(

            0,

            min(

                item.score,

                100

            )

        )



        item.importance = (

            3

            if item.score >= 70

            else

            2

            if item.score >= 50

            else

            1

        )


        return item



# ============================================================
# KAP SERVICE
# ============================================================


class KAPService:


    def __init__(self):

        self.analyzer = KAPAnalyzer()
        self.provider = kap_provider


    def fetch(self, symbol: str):

        logger.info(
            "Searching KAP for %s",
            symbol
        )

        raw_items = self.provider.fetch(
            symbol.upper()
        )

        normalized = self.provider.normalize(
            raw_items,
            symbol.upper()
        )

        return [

            KAPItem(**item)

            for item in normalized

        ]



    def analyze(

        self,

        items: List[KAPItem],

    ):


        return [

            self.analyzer.analyze(item)

            for item in items

        ]



    def statistics(

        self,

        items: List[KAPItem],

    ):


        return {


            "total":

            len(items),


            "high":

            len(

                [

                    x

                    for x in items

                    if x.importance == 3

                ]

            ),


            "medium":

            len(

                [

                    x

                    for x in items

                    if x.importance == 2

                ]

            ),


            "low":

            len(

                [

                    x

                    for x in items

                    if x.importance == 1

                ]

            ),


            "average_score":

            round(

                sum(

                    x.score

                    for x in items

                )

                /

                len(items),

                2

            )

            if items

            else 0,

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

                asdict(x)

                for x in items

            ],


            "statistics":

            self.statistics(

                items

            ),


            "generated_at":

            datetime.utcnow().isoformat(),

        }



# ============================================================
# SINGLETON
# ============================================================


kap_service = KAPService()



# ============================================================
# PUBLIC API
# ============================================================


def get_kap(

    symbol: str,

):


    return kap_service.fetch(

        symbol

    )



def kap_dashboard(

    symbol: str,

):


    return kap_service.dashboard(

        symbol

    )



def kap_health():


    return {


        "service":

        "KAP Intelligence",


        "status":

        "ok",

    }



__all__ = [

    "KAPItem",

    "KAPService",

    "kap_service",

    "get_kap",

    "kap_dashboard",

    "kap_health",

]
# backward compatibility
KapService = KAPService