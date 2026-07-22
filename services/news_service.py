"""
News Service
BIST AI LAB v10.0 Professional AI News Engine
"""

from __future__ import annotations

from dataclasses import dataclass

from data.google_news_provider import GoogleNewsProvider
from services.sentiment_service import SentimentService
from services.news_ai_service import NewsAIService


SYMBOL_MAP = {

    "ASELS": "ASELSAN",
    "ASELS.IS": "ASELSAN",

    "THYAO": "Turkish Airlines",
    "THYAO.IS": "Turkish Airlines",

    "KCHOL": "Koç Holding",
    "KCHOL.IS": "Koç Holding",

    "SISE": "Şişecam",
    "SISE.IS": "Şişecam",

    "TUPRS": "Tüpraş",
    "TUPRS.IS": "Tüpraş",

    "AKBNK": "Akbank",
    "AKBNK.IS": "Akbank",

    "GARAN": "Garanti BBVA",
    "GARAN.IS": "Garanti BBVA",

    "EREGL": "Erdemir",
    "EREGL.IS": "Erdemir",

    "BIMAS": "BİM",
    "BIMAS.IS": "BİM",

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

    category: str

    relevance: float


class NewsService:

    def __init__(self):

        self.provider = GoogleNewsProvider()

        self.sentiment = SentimentService()

        self.ai = NewsAIService()

    # =====================================================

    def _category(self, title: str):

        t = title.lower()

        if any(

            x in t

            for x in [

                "aselsan",

                "thy",

                "akbank",

                "garan",

                "koç",

                "sisecam",

                "şişecam",

                "erdemir",

                "tüpraş",

                "bim",

            ]

        ):

            return "COMPANY", 100

        if any(

            x in t

            for x in [

                "defense",

                "savunma",

                "bank",

                "steel",

                "energy",

                "oil",

                "drone",

                "radar",

                "air defense",

                "market",

            ]

        ):

            return "SECTOR", 85

        if any(

            x in t

            for x in [

                "fed",

                "inflation",

                "interest",

                "economy",

                "gdp",

                "growth",

            ]

        ):

            return "MACRO", 70

        if any(

            x in t

            for x in [

                "nato",

                "war",

                "ukraine",

                "russia",

                "china",

                "iran",

                "israel",

            ]

        ):

            return "GEOPOLITICAL", 65

        return "OTHER", 40

    # =====================================================

    def get_news(self, symbol: str):

        keyword = SYMBOL_MAP.get(

            symbol.upper(),

            symbol,

        )

        print("=" * 80)
        print("NEWS SEARCH")
        print("SYMBOL :", symbol)
        print("KEYWORD:", keyword)

        articles = self.provider.search(keyword)
        titles = []
        if index < len(ai_results):

            ai = ai_results[index]

        else:

            ai = {}
        for index, article in enumerate(articles):

            title = article.get("title", "").strip()

            if title:

                titles.append(title)

        ai_results = self.ai.analyze(titles)

        print("ARTICLE COUNT:", len(articles))

        results = []

        for article in articles:

            try:

                title = article.get(

                    "title",

                    "",

                ).strip()

                if not title:

                    continue

                sentiment = self.sentiment.analyze(title)

                

                source = article.get(

                    "source",

                    {},

                )

                if isinstance(source, dict):

                    source_name = source.get(

                        "name",

                        "Unknown",

                    )

                else:

                    source_name = str(source)

                category, relevance = self._category(title)

                score = float(

                    sentiment.get(

                        "score",

                        50,

                    )

                )

                score = (

                    score * 0.50

                    + relevance * 0.30

                    + ai.get(

                        "importance",

                        3,

                    ) * 20 * 0.20

                )

                results.append(

                    NewsResult(

                        source=source_name,

                        title=title,

                        title_tr=ai.get(

                            "title_tr",

                            title,

                        ),

                        summary=ai.get(

                            "summary",

                            "",

                        ),

                        market_effect=ai.get(

                            "market_effect",

                            "NOTR",

                        ),

                        importance=int(

                            ai.get(

                                "importance",

                                3,

                            )

                        ),

                        ai_comment=ai.get(

                            "ai_comment",

                            "",

                        ),

                        url=article.get(

                            "url",

                            "",

                        ),

                        sentiment=sentiment.get(

                            "sentiment",

                            "NEUTRAL",

                        ),

                        score=round(

                            score,

                            2,

                        ),

                        category=category,

                        relevance=relevance,

                    )

                )

            except Exception as e:

                import traceback

                print("=" * 80)
                print("NEWS ERROR")
                print(e)
                traceback.print_exc()
                print("=" * 80)

        results.sort(

            key=lambda x: (

                x.relevance,

                x.importance,

                x.score,

            ),

            reverse=True,

        )

        filtered = []

        titles = set()

        for item in results:

            key = item.title.lower()

            if key in titles:

                continue

            titles.add(key)

            filtered.append(item)

        print("FINAL NEWS:", len(filtered))

        return filtered