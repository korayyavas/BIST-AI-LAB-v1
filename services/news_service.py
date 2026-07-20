"""
News Service
BIST AI LAB v8
"""

from __future__ import annotations

from dataclasses import dataclass

from core.cache_manager import CacheManager

from data.google_news_provider import GoogleNewsProvider
from services.sentiment_service import SentimentService


SYMBOL_MAP = {
    "ASELS.IS": "ASELSAN",
    "THYAO.IS": "Turkish Airlines",
    "KCHOL.IS": "Koç Holding",
    "SISE.IS": "Şişecam",
    "TUPRS.IS": "Tüpraş",
    "AKBNK.IS": "Akbank",
    "GARAN.IS": "Garanti BBVA",
    "EREGL.IS": "Erdemir",
    "BIMAS.IS": "BİM",
}


@dataclass
class NewsResult:

    source: str

    title: str

    url: str

    sentiment: str

    score: float


class NewsService:

    def __init__(self):

        self.provider = GoogleNewsProvider()

        self.sentiment = SentimentService()

        self.cache = CacheManager()

    # =====================================================

    def get_news(self, symbol: str):

        def producer():

            keyword = SYMBOL_MAP.get(symbol, symbol)

            articles = self.provider.search(keyword)

            news = []

            for article in articles:

                title = article.get("title", "")

                analysis = self.sentiment.analyze(title)

                source = article.get("source", {})

                if isinstance(source, dict):

                    source_name = source.get(
                        "name",
                        "Unknown",
                    )

                else:

                    source_name = "Unknown"

                news.append(

                    NewsResult(

                        source=source_name,

                        title=title,

                        url=article.get(
                            "url",
                            "",
                        ),

                        sentiment=analysis["sentiment"],

                        score=analysis["score"],

                    )

                )

            return [

                item.__dict__

                for item in news

            ]

        cached = self.cache.get(

            f"news_{symbol}",

            producer,

        )

        return [

            NewsResult(**item)

            for item in cached

        ]