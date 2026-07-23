from __future__ import annotations

"""
services/news_service.py

BIST AI LAB
Professional AI News Engine v2.1

AI Translation Matching Fix
"""

from dataclasses import asdict, dataclass, field

import asyncio
import hashlib
import logging
import re

from collections import defaultdict

from datetime import datetime, timedelta

from enum import Enum

from typing import Any, Dict, Iterable, List, Optional, Set


import httpx


from data.google_news_provider import GoogleNewsProvider

from services.news_ai_service import NewsAIService

from services.sentiment_service import SentimentService



logger = logging.getLogger(__name__)




DEFAULT_TIMEOUT = 20

CACHE_MINUTES = 10

MAX_NEWS = 50




SYMBOL_MAP = {

    "ASELS": "ASELSAN",

    "THYAO": "Turkish Airlines",

    "KCHOL": "Koç Holding",

    "SISE": "Şişecam",

    "TUPRS": "Tüpraş",

    "AKBNK": "Akbank",

    "GARAN": "Garanti BBVA",

    "EREGL": "Erdemir",

    "BIMAS": "BİM",

}




class NewsCategory(str, Enum):

    COMPANY="COMPANY"

    SECTOR="SECTOR"

    MACRO="MACRO"

    GEOPOLITICAL="GEOPOLITICAL"

    OTHER="OTHER"





@dataclass(slots=True)
class NewsArticle:

    source:str

    title:str

    url:str

    published:Optional[datetime]=None

    summary:str=""

    raw:Dict[str,Any]=field(default_factory=dict)





@dataclass(slots=True)
class AIAnalysis:

    title_tr:str=""

    summary:str=""

    ai_comment:str=""

    market_effect:str="UNKNOWN"

    importance:int=3





@dataclass(slots=True)
class NewsResult:

    source:str

    title:str

    title_tr:str

    summary:str

    market_effect:str

    importance:int

    ai_comment:str

    url:str

    sentiment:str

    score:float

    category:str

    relevance:float





class NewsCache:


    def __init__(self):

        self.data={}

        self.expire={}



    def get(self,key):

        if key not in self.data:

            return None


        if datetime.utcnow()>self.expire[key]:

            self.data.pop(key,None)

            return None


        return self.data[key]




    def put(self,key,value):

        self.data[key]=value

        self.expire[key]=datetime.utcnow()+timedelta(

            minutes=CACHE_MINUTES

        )




    def clear(self):

        self.data.clear()

        self.expire.clear()





def normalize(text):

    if not text:

        return ""

    text=re.sub(

        r"\s+",

        " ",

        text

    )

    return text.strip()





def make_key(text):

    return hashlib.md5(

        normalize(text).lower().encode()

    ).hexdigest()




def unique_articles(items):

    seen=set()

    result=[]


    for item in items:

        key=make_key(item.title)

        if key in seen:

            continue


        seen.add(key)

        result.append(item)



    return result
# ============================================================
# AI ENGINE
# ============================================================


class AIEngine:


    def __init__(self):

        self.service = NewsAIService()



    def analyze(self, titles):


        if not titles:

            return []



        try:

            response = self.service.analyze(

                titles

            )


        except Exception as e:


            logger.exception(

                "AI news analysis failed %s",

                e

            )

            return []



        result=[]



        for item in response:


            result.append(

                AIAnalysis(

                    title_tr=item.get(

                        "title_tr",

                        ""

                    ),

                    summary=item.get(

                        "summary",

                        ""

                    ),

                    ai_comment=item.get(

                        "ai_comment",

                        ""

                    ),

                    market_effect=item.get(

                        "market_effect",

                        "UNKNOWN"

                    ),

                    importance=int(

                        item.get(

                            "importance",

                            3

                        )

                    )

                )

            )


        return result







# ============================================================
# AI MATCH ENGINE
# ============================================================


class AIMatchEngine:


    @staticmethod
    def match(

        article,

        ai_results

    ):


        if not ai_results:

            return None



        source_title = normalize(

            article.title

        ).lower()



        best=None

        score=0



        for item in ai_results:


            ai_title = normalize(

                item.title_tr

            ).lower()



            if not ai_title:

                continue



            current=0



            words = ai_title.split()



            for word in words:


                if word in source_title:

                    current += 1



            if current > score:


                score=current

                best=item




        return best

# ============================================================
# CATEGORY ENGINE
# ============================================================

class CategoryEngine:


    @staticmethod
    def classify(title):


        text = normalize(title).lower()


        if any(
            x in text
            for x in [
                "aselsan",
                "şirket",
                "company",
                "contract",
                "agreement",
                "sözleşme"
            ]
        ):

            return (
                NewsCategory.COMPANY,
                90
            )



        if any(
            x in text
            for x in [
                "nato",
                "savunma",
                "defense",
                "military",
                "drone"
            ]
        ):

            return (
                NewsCategory.SECTOR,
                80
            )



        if any(
            x in text
            for x in [
                "enflasyon",
                "faiz",
                "merkez bankası",
                "fed",
                "ecb"
            ]
        ):

            return (
                NewsCategory.MACRO,
                70
            )



        if any(
            x in text
            for x in [
                "savaş",
                "kriz",
                "jeopolitik",
                "geopolitical"
            ]
        ):

            return (
                NewsCategory.GEOPOLITICAL,
                75
            )


        return (

            NewsCategory.OTHER,

            50

        )    
    # ============================================================
# RESULT BUILDER
# ============================================================


class ResultBuilder:


    @staticmethod
    def build(

        article,

        sentiment,

        ai,

    ):


        category, relevance = (

            CategoryEngine.classify(

                article.title

            )

        )


        importance = (

            ai.importance

            if ai

            else 3

        )



        score = (

            float(

                sentiment.get(

                    "score",

                    50

                )

            )

            + relevance

            + (importance * 10)

        ) / 3



        return NewsResult(

            source=article.source,

            title=article.title,


            title_tr=(

                ai.title_tr

                if ai and ai.title_tr

                else article.title

            ),



            summary=(

                ai.summary

                if ai and ai.summary

                else article.summary

            ),



            market_effect=(

                ai.market_effect

                if ai

                else "UNKNOWN"

            ),



            importance=importance,



            ai_comment=(

                ai.ai_comment

                if ai

                else ""

            ),



            url=article.url,



            sentiment=sentiment.get(

                "sentiment",

                "NEUTRAL"

            ),



            score=round(

                score,

                2

            ),



            category=category.value,



            relevance=relevance,

        )






# ============================================================
# NEWS SERVICE
# ============================================================


class NewsService:


    def __init__(self):


        self.cache=NewsCache()


        self.ai=AIEngine()


        self.sentiment=SentimentService()



    def keyword(self,symbol):


        return SYMBOL_MAP.get(

            symbol.upper(),

            symbol

        )




    def get_news(self,symbol):


        key=symbol.upper()



        cached=self.cache.get(key)


        if cached is not None:

            return cached




        keyword=self.keyword(symbol)



        logger.info(

            "Searching news for %s",

            keyword

        )



        provider=GoogleNewsProvider()



        raw=provider.search(

            keyword

        )



        articles=[]



        for item in raw:


            articles.append(

                NewsArticle(

                    source=item.get(

                        "source",

                        "Google"

                    )

                    if isinstance(

                        item.get("source"),

                        str

                    )

                    else item.get(

                        "source",

                        {}

                    ).get(

                        "name",

                        "Google"

                    ),



                    title=normalize(

                        item.get(

                            "title",

                            ""

                        )

                    ),



                    url=item.get(

                        "url",

                        ""

                    ),



                    summary=item.get(

                        "description",

                        ""

                    ),



                    raw=item

                )

            )





        articles=unique_articles(

            articles

        )



        titles=[

            x.title

            for x in articles

        ]




        ai_results=self.ai.analyze(

            titles

        )




        results=[]



        for article in articles:



            sentiment=self.sentiment.analyze(

                article.title

            )



            ai=AIMatchEngine.match(

                article,

                ai_results

            )



            results.append(

                ResultBuilder.build(

                    article,

                    sentiment,

                    ai

                )

            )




        results.sort(

            key=lambda x:x.score,

            reverse=True

        )



        results=results[:50]



        self.cache.put(

            key,

            results

        )



        logger.info(

            "%s news returned",

            len(results)

        )



        return results





# ============================================================
# SINGLETON
# ============================================================


news_service=NewsService()






# ============================================================
# EXPORT
# ============================================================


def get_news(symbol):

    return news_service.get_news(

        symbol

    )





def news_dashboard(symbol):


    items=get_news(symbol)



    return {


        "symbol":symbol.upper(),


        "news":[

            asdict(x)

            for x in items

        ],



        "statistics":{


            "total":len(items)


        },



        "generated_at":

        datetime.utcnow().isoformat()

    }





def clear_news_cache():

    news_service.cache.clear()




def news_health():


    return {


        "service":"news",

        "status":"ok"

    }




__all__=[

    "NewsService",

    "NewsResult",

    "get_news",

    "search_news",

    "news_dashboard",

    "clear_news_cache",

    "news_health"

]
def search_news(symbol):

    return news_service.get_news(

        symbol

    )