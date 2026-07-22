"""
News Service
BIST AI LAB v9
"""

from __future__ import annotations

from dataclasses import dataclass

from data.google_news_provider import GoogleNewsProvider
from services.sentiment_service import SentimentService
from services.news_ai_service import NewsAIService


SYMBOL_MAP = {
    "ASELS.IS": "ASELSAN",
    "ASELS": "ASELSAN",
    "THYAO.IS": "Turkish Airlines",
    "THYAO": "Turkish Airlines",
    "KCHOL.IS": "Koç Holding",
    "KCHOL": "Koç Holding",
    "SISE.IS": "Şişecam",
    "SISE": "Şişecam",
    "TUPRS.IS": "Tüpraş",
    "TUPRS": "Tüpraş",
    "AKBNK.IS": "Akbank",
    "AKBNK": "Akbank",
    "GARAN.IS": "Garanti BBVA",
    "GARAN": "Garanti BBVA",
    "EREGL.IS": "Erdemir",
    "EREGL": "Erdemir",
    "BIMAS.IS": "BİM",
    "BIMAS": "BİM",
}


@dataclass
class NewsResult:

    source: str

    title: str

    title_tr: str

    summary: str

    market_effect: str

    importance: int

    ai_comment: str

    url: str

    sentiment: str

    score: float


class NewsService:

    def __init__(self):

        self.provider = GoogleNewsProvider()

        self.sentiment = SentimentService()

        self.ai = NewsAIService()

    # =====================================================

    def get_news(self, symbol: str):

        keyword = SYMBOL_MAP.get(symbol.upper(), symbol)

        print("=" * 80)
        print("NEWS SEARCH")
        print("SYMBOL :", symbol)
        print("KEYWORD:", keyword)

        articles = self.provider.search(keyword)

        print("ARTICLE COUNT:", len(articles))

        news = []

        for article in articles:

            try:

                title = article.get("title", "").strip()

                if not title:
                    continue

                sentiment = self.sentiment.analyze(title)

                ai = self.ai.analyze(title)

                source = article.get("source", {})

                if isinstance(source, dict):

                    source_name = source.get(
                        "name",
                        "Unknown",
                    )

                else:

                    source_name = str(source)

                news.append(

                    NewsResult(

                        source=source_name,

                        title=title,

                        title_tr=ai["title_tr"],

                        summary=ai["summary"],

                        market_effect=ai["market_effect"],

                        importance=ai["importance"],

                        ai_comment=ai["ai_comment"],

                        url=article.get(
                            "url",
                            "",
                        ),

                        sentiment=sentiment["sentiment"],

                        score=sentiment["score"],

                    )

                )

            except Exception as e:

                print("=" * 80)
                print("NEWS ERROR")
                print(e)
                print("=" * 80)

        print("FINAL NEWS:", len(news))
        print("=" * 80)

        return news