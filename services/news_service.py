from __future__ import annotations

"""
services/news_service.py

BIST AI LAB
Professional AI News Engine v2

PART 1
"""


from dataclasses import asdict


import asyncio
import hashlib
import logging
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, Iterable, List, Optional, Set

import httpx

from data.google_news_provider import GoogleNewsProvider
from services.news_ai_service import NewsAIService
from services.sentiment_service import SentimentService

logger = logging.getLogger(__name__)


# ============================================================
# CONSTANTS
# ============================================================

DEFAULT_TIMEOUT = 20
CACHE_MINUTES = 10
MAX_NEWS = 50
MAX_TITLE_LENGTH = 500


SYMBOL_MAP: Dict[str, str] = {

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


# ============================================================
# ENUMS
# ============================================================


class NewsCategory(str, Enum):

    COMPANY = "COMPANY"

    SECTOR = "SECTOR"

    MACRO = "MACRO"

    GEOPOLITICAL = "GEOPOLITICAL"

    OTHER = "OTHER"


class MarketEffect(str, Enum):

    POSITIVE = "POSITIVE"

    NEGATIVE = "NEGATIVE"

    NEUTRAL = "NEUTRAL"

    UNKNOWN = "UNKNOWN"


class NewsSentiment(str, Enum):

    POSITIVE = "POSITIVE"

    NEGATIVE = "NEGATIVE"

    NEUTRAL = "NEUTRAL"


# ============================================================
# DATA MODELS
# ============================================================


@dataclass(slots=True)
class NewsArticle:

    source: str

    title: str

    url: str

    published: Optional[datetime] = None

    summary: str = ""

    language: str = "en"

    symbol: str = ""

    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AIAnalysis:

    title_tr: str = ""

    summary: str = ""

    ai_comment: str = ""

    market_effect: str = "UNKNOWN"

    importance: int = 3


@dataclass(slots=True)
class ScoreCard:

    sentiment_score: float = 50

    relevance_score: float = 40

    ai_score: float = 60

    final_score: float = 50


@dataclass(slots=True)
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


# ============================================================
# SIMPLE MEMORY CACHE
# ============================================================


class NewsCache:

    def __init__(self):

        self._cache: Dict[str, Any] = {}

        self._expires: Dict[str, datetime] = {}

    def _expired(self, key: str) -> bool:

        exp = self._expires.get(key)

        if exp is None:
            return True

        return datetime.utcnow() >= exp

    def get(self, key: str):

        if self._expired(key):

            self._cache.pop(key, None)

            self._expires.pop(key, None)

            return None

        return self._cache.get(key)

    def put(
        self,
        key: str,
        value: Any,
        minutes: int = CACHE_MINUTES,
    ):

        self._cache[key] = value

        self._expires[key] = (
            datetime.utcnow()
            + timedelta(minutes=minutes)
        )

    def clear(self):

        self._cache.clear()

        self._expires.clear()


# ============================================================
# HTTP CLIENT
# ============================================================


class HTTPClient:

    def __init__(self):

        self.client = httpx.Client(

            timeout=DEFAULT_TIMEOUT,

            follow_redirects=True,

            headers={

                "User-Agent":
                "BIST AI LAB Professional News Engine"

            }

        )

    def get(self, url: str):

        return self.client.get(url)

    def close(self):

        self.client.close()


# ============================================================
# TEXT HELPERS
# ============================================================


_whitespace = re.compile(r"\s+")

_html = re.compile(r"<[^>]+>")


def normalize(text: str) -> str:

    if not text:

        return ""

    text = _html.sub("", text)

    text = _whitespace.sub(" ", text)

    return text.strip()


def make_key(title: str) -> str:

    return hashlib.md5(

        normalize(title).lower().encode()

    ).hexdigest()


def unique_articles(
    articles: Iterable[NewsArticle],
) -> List[NewsArticle]:

    seen: Set[str] = set()

    result: List[NewsArticle] = []

    for article in articles:

        key = make_key(article.title)

        if key in seen:

            continue

        seen.add(key)

        result.append(article)

    return result

# ============================================================
# CATEGORY ENGINE
# ============================================================


class CategoryEngine:

    COMPANY_KEYWORDS = {

        "aselsan",
        "thy",
        "thyao",
        "turkish airlines",
        "akbank",
        "garan",
        "garanti",
        "koç",
        "koc",
        "holding",
        "şişecam",
        "sisecam",
        "erdemir",
        "eregl",
        "tüpraş",
        "tupras",
        "bim",
        "bimas",

    }

    SECTOR_KEYWORDS = {

        "bank",

        "banking",

        "finance",

        "financial",

        "energy",

        "oil",

        "gas",

        "steel",

        "cement",

        "aviation",

        "airline",

        "defense",

        "savunma",

        "drone",

        "radar",

        "missile",

        "air defense",

        "technology",

        "chip",

        "factory",

    }

    MACRO_KEYWORDS = {

        "fed",

        "ecb",

        "tcmb",

        "interest",

        "inflation",

        "economy",

        "economic",

        "gdp",

        "growth",

        "unemployment",

        "employment",

        "ppi",

        "cpi",

        "export",

        "import",

        "usd",

        "eur",

        "gold",

        "oil price",

    }

    GEO_KEYWORDS = {

        "war",

        "ukraine",

        "russia",

        "china",

        "iran",

        "israel",

        "nato",

        "usa",

        "sanction",

        "conflict",

        "missile",

        "middle east",

    }

    @classmethod
    def classify(cls, title: str):

        t = normalize(title).lower()

        if any(x in t for x in cls.COMPANY_KEYWORDS):

            return NewsCategory.COMPANY, 100

        if any(x in t for x in cls.SECTOR_KEYWORDS):

            return NewsCategory.SECTOR, 85

        if any(x in t for x in cls.MACRO_KEYWORDS):

            return NewsCategory.MACRO, 70

        if any(x in t for x in cls.GEO_KEYWORDS):

            return NewsCategory.GEOPOLITICAL, 65

        return NewsCategory.OTHER, 40


# ============================================================
# SCORE ENGINE
# ============================================================


class ScoreEngine:

    SENTIMENT_WEIGHT = 0.50

    RELEVANCE_WEIGHT = 0.30

    AI_WEIGHT = 0.20

    @classmethod
    def calculate(

        cls,

        sentiment_score: float,

        relevance: float,

        importance: int,

    ) -> ScoreCard:

        ai_score = importance * 20

        final = (

            sentiment_score * cls.SENTIMENT_WEIGHT

            + relevance * cls.RELEVANCE_WEIGHT

            + ai_score * cls.AI_WEIGHT

        )

        return ScoreCard(

            sentiment_score=sentiment_score,

            relevance_score=relevance,

            ai_score=ai_score,

            final_score=round(final, 2),

        )


# ============================================================
# GOOGLE PROVIDER ADAPTER
# ============================================================


class GoogleProvider:

    def __init__(self):

        self.provider = GoogleNewsProvider()

    def search(

        self,

        keyword: str,

    ) -> List[NewsArticle]:

        raw = self.provider.search(keyword)

        news: List[NewsArticle] = []

        for item in raw:

            title = normalize(

                item.get("title", "")

            )

            if not title:

                continue

            source = item.get(

                "source",

                {},

            )

            if isinstance(source, dict):

                source = source.get(

                    "name",

                    "Google",

                )

            news.append(

                NewsArticle(

                    source=str(source),

                    title=title,

                    url=item.get(

                        "url",

                        "",

                    ),

                    summary=item.get(

                        "description",

                        "",

                    ),

                    raw=item,

                )

            )

        return unique_articles(news)


# ============================================================
# SENTIMENT ADAPTER
# ============================================================


class SentimentEngine:

    def __init__(self):

        self.service = SentimentService()

    def analyze(

        self,

        article: NewsArticle,

    ):

        try:

            return self.service.analyze(

                article.title

            )

        except Exception:

            logger.exception(

                "Sentiment failed"

            )

            return {

                "sentiment": "NEUTRAL",

                "score": 50,

            }


# ============================================================
# AI ENGINE
# ============================================================


class AIEngine:

    def __init__(self):

        self.service = NewsAIService()

    def analyze(

        self,

        titles: List[str],

    ) -> List[AIAnalysis]:

        if not titles:

            return []

        try:

            result = self.service.analyze(

                titles

            )

        except Exception:

            logger.exception(

                "AI analyze failed"

            )

            result = []

        analyses: List[AIAnalysis] = []

        for item in result:

            analyses.append(

                AIAnalysis(

                    title_tr=item.get(

                        "title_tr",

                        "",

                    ),

                    summary=item.get(

                        "summary",

                        "",

                    ),

                    ai_comment=item.get(

                        "ai_comment",

                        "",

                    ),

                    market_effect=item.get(

                        "market_effect",

                        "UNKNOWN",

                    ),

                    importance=int(

                        item.get(

                            "importance",

                            3,

                        )

                    ),

                )

            )

        return analyses

    # ============================================================
# NEWS AGGREGATOR
# ============================================================


class NewsAggregator:

    def __init__(self):

        self.google = GoogleProvider()

    def collect(

        self,

        keyword: str,

    ) -> List[NewsArticle]:

        articles: List[NewsArticle] = []

        try:

            articles.extend(

                self.google.search(

                    keyword

                )

            )

        except Exception:

            logger.exception(

                "Google provider failed"

            )

        articles = unique_articles(

            articles

        )

        articles.sort(

            key=lambda x: x.title

        )

        return articles


# ============================================================
# RESULT BUILDER
# ============================================================


class ResultBuilder:

    @staticmethod
    def build(

        article: NewsArticle,

        sentiment: Dict[str, Any],

        ai: Optional[AIAnalysis],

    ) -> NewsResult:

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

        score = ScoreEngine.calculate(

            float(

                sentiment.get(

                    "score",

                    50,

                )

            ),

            relevance,

            importance,

        )

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
                if ai
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

                "NEUTRAL",

            ),

            score=score.final_score,

            category=category.value,

            relevance=relevance,

        )


# ============================================================
# NEWS SERVICE
# ============================================================


class NewsService:

    def __init__(self):

        self.cache = NewsCache()

        self.sentiment = SentimentEngine()

        self.ai = AIEngine()

        self.aggregator = NewsAggregator()

    # --------------------------------------------------------

    def _keyword(

        self,

        symbol: str,

    ) -> str:

        return SYMBOL_MAP.get(

            symbol.upper(),

            symbol,

        )

    # --------------------------------------------------------

    def _cache_key(

        self,

        symbol: str,

    ) -> str:

        return symbol.upper()

    # --------------------------------------------------------

    def get_news(

        self,

        symbol: str,

    ) -> List[NewsResult]:

        key = self._cache_key(

            symbol

        )

        cached = self.cache.get(

            key

        )

        if cached is not None:

            return cached

        keyword = self._keyword(

            symbol

        )

        logger.info(

            "Searching news for %s",

            keyword,

        )

        articles = (

            self.aggregator.collect(

                keyword

            )

        )

        if not articles:

            self.cache.put(

                key,

                [],

            )

            return []

        titles = [

            x.title

            for x in articles

        ]

        ai_results = self.ai.analyze(

            titles

        )

        results: List[NewsResult] = []

        for index, article in enumerate(

            articles

        ):

            sentiment = (

                self.sentiment.analyze(

                    article

                )

            )

            ai = (

                ai_results[index]

                if index < len(ai_results)

                else None

            )

            results.append(

                ResultBuilder.build(

                    article,

                    sentiment,

                    ai,

                )

            )

        results.sort(

            key=lambda x: (

                x.score,

                x.relevance,

                x.importance,

            ),

            reverse=True,

        )

        if len(results) > MAX_NEWS:

            results = results[:MAX_NEWS]

        self.cache.put(

            key,

            results,

        )

        logger.info(

            "%d news returned",

            len(results),

        )

        return results

    # --------------------------------------------------------

    def clear_cache(self):

        self.cache.clear()

    # --------------------------------------------------------

    def health(self):

        return {

            "service": "news",

            "status": "ok",

            "provider": "Google News",

            "cache_entries": len(

                self.cache._cache

            ),

        }


# ============================================================
# SINGLETON
# ============================================================

news_service = NewsService()


# ============================================================
# PUBLIC API
# ============================================================


def get_news(

    symbol: str,

) -> List[NewsResult]:

    return news_service.get_news(

        symbol

    )


def clear_news_cache():

    news_service.clear_cache()


def news_health():

    return news_service.health()

# ============================================================
# ADVANCED FILTERS
# ============================================================


class NewsFilter:

    @staticmethod
    def remove_empty(

        news: List[NewsResult],

    ) -> List[NewsResult]:

        return [

            x

            for x in news

            if x.title.strip()

        ]

    @staticmethod
    def remove_duplicate_titles(

        news: List[NewsResult],

    ) -> List[NewsResult]:

        seen = set()

        result = []

        for item in news:

            key = normalize(

                item.title

            ).lower()

            if key in seen:

                continue

            seen.add(key)

            result.append(item)

        return result

    @staticmethod
    def minimum_score(

        news: List[NewsResult],

        score: float,

    ) -> List[NewsResult]:

        return [

            x

            for x in news

            if x.score >= score

        ]

    @staticmethod
    def category(

        news: List[NewsResult],

        category: NewsCategory,

    ):

        return [

            x

            for x in news

            if x.category == category.value

        ]

    @staticmethod
    def sentiment(

        news: List[NewsResult],

        sentiment: str,

    ):

        sentiment = sentiment.upper()

        return [

            x

            for x in news

            if x.sentiment.upper()

            == sentiment

        ]


# ============================================================
# TREND ENGINE
# ============================================================


class TrendEngine:

    STOP_WORDS = {

        "the",

        "and",

        "of",

        "for",

        "with",

        "from",

        "will",

        "after",

        "about",

        "this",

        "that",

        "into",

        "have",

        "has",

        "had",

        "more",

        "less",

        "its",

        "their",

        "they",

        "his",

        "her",

        "our",

        "new",

        "shares",

        "stock",

        "company",

    }

    @classmethod
    def keywords(

        cls,

        news: List[NewsResult],

        top: int = 20,

    ):

        words = defaultdict(int)

        for item in news:

            tokens = re.findall(

                r"[A-Za-zÇĞİÖŞÜçğıöşü0-9]{3,}",

                item.title,

            )

            for token in tokens:

                token = token.lower()

                if token in cls.STOP_WORDS:

                    continue

                words[token] += 1

        return sorted(

            words.items(),

            key=lambda x: x[1],

            reverse=True,

        )[:top]


# ============================================================
# STATISTICS
# ============================================================


class NewsStatistics:

    @staticmethod
    def summary(

        news: List[NewsResult],

    ):

        stats = {

            "total": len(news),

            "positive": 0,

            "negative": 0,

            "neutral": 0,

            "average_score": 0,

            "categories": defaultdict(int),

        }

        total_score = 0.0

        for item in news:

            total_score += item.score

            s = item.sentiment.upper()

            if s == "POSITIVE":

                stats["positive"] += 1

            elif s == "NEGATIVE":

                stats["negative"] += 1

            else:

                stats["neutral"] += 1

            stats["categories"][

                item.category

            ] += 1

        if news:

            stats["average_score"] = round(

                total_score / len(news),

                2,

            )

        stats["categories"] = dict(

            stats["categories"]

        )

        return stats


# ============================================================
# EXPORTERS
# ============================================================


class NewsExporter:

    @staticmethod
    def to_dict(

        news: List[NewsResult],

    ):

        return [

            {

                "source": x.source,

                "title": x.title,

                "title_tr": x.title_tr,

                "summary": x.summary,

                "market_effect": x.market_effect,

                "importance": x.importance,

                "ai_comment": x.ai_comment,

                "url": x.url,

                "sentiment": x.sentiment,

                "score": x.score,

                "category": x.category,

                "relevance": x.relevance,

            }

            for x in news

        ]

    @staticmethod
    def dataframe(

        news: List[NewsResult],

    ):

        try:

            import pandas as pd

            return pd.DataFrame(

                NewsExporter.to_dict(

                    news

                )

            )

        except Exception:

            logger.exception(

                "Pandas export failed"

            )

            return None

        # ============================================================
# ASYNC API
# ============================================================


class AsyncNewsService:

    def __init__(self):

        self.service = news_service

    async def get_news(

        self,

        symbol: str,

    ) -> List[NewsResult]:

        return await asyncio.to_thread(

            self.service.get_news,

            symbol,

        )

    async def health(self):

        return await asyncio.to_thread(

            self.service.health

        )


async_news_service = AsyncNewsService()


# ============================================================
# SEARCH
# ============================================================


def search_news(

    symbol: str,

    minimum_score: float = 0,

    category: Optional[NewsCategory] = None,

    sentiment: Optional[str] = None,

) -> List[NewsResult]:

    news = get_news(symbol)

    news = NewsFilter.remove_empty(news)

    news = NewsFilter.remove_duplicate_titles(news)

    if minimum_score > 0:

        news = NewsFilter.minimum_score(

            news,

            minimum_score,

        )

    if category:

        news = NewsFilter.category(

            news,

            category,

        )

    if sentiment:

        news = NewsFilter.sentiment(

            news,

            sentiment,

        )

    return news


# ============================================================
# DASHBOARD API
# ============================================================


def dashboard(

    symbol: str,

) -> Dict[str, Any]:

    news = get_news(symbol)

    return {

        "symbol": symbol,

        "news": NewsExporter.to_dict(

            news

        ),

        "statistics": NewsStatistics.summary(

            news

        ),

        "trending": TrendEngine.keywords(

            news

        ),

        "generated_at": datetime.utcnow().isoformat(),

    }


# ============================================================
# TEST
# ============================================================


if __name__ == "__main__":

    logging.basicConfig(

        level=logging.INFO,

        format="%(levelname)s | %(message)s",

    )

    symbol = "ASELS"

    result = dashboard(symbol)

    print("=" * 80)

    print("NEWS ENGINE")

    print("=" * 80)

    print(

        "News:",

        len(result["news"]),

    )

    print(

        "Statistics:",

        result["statistics"],

    )

    print(

        "Trending:",

        result["trending"][:10],

    )

    print("=" * 80)

    for item in result["news"][:5]:

        print()

        print(item["title"])

        print(item["title_tr"])

        print(item["score"])

        print(item["sentiment"])

        print(item["market_effect"])

        print(item["url"])


# ============================================================
# EXPORTS
# ============================================================

__all__ = [

    "NewsArticle",

    "NewsResult",

    "NewsService",

    "NewsFilter",

    "NewsStatistics",

    "NewsExporter",

    "TrendEngine",

    "CategoryEngine",

    "ScoreEngine",

    "NewsCache",

    "NewsCategory",

    "NewsSentiment",

    "MarketEffect",

    "news_service",

    "async_news_service",

    "get_news",

    "search_news",

    "dashboard",

    "clear_news_cache",

    "news_health",

    "news_dashboard",

]

# ============================================================
# FUTURE EXTENSIONS
# ============================================================


class NewsMetrics:

    @staticmethod
    def average_score(news: List[NewsResult]) -> float:

        if not news:

            return 0.0

        return round(

            sum(x.score for x in news)

            / len(news),

            2,

        )

    @staticmethod
    def strongest_positive(

        news: List[NewsResult],

    ) -> Optional[NewsResult]:

        positive = [

            x

            for x in news

            if x.sentiment.upper()

            == "POSITIVE"

        ]

        if not positive:

            return None

        return max(

            positive,

            key=lambda x: x.score,

        )

    @staticmethod
    def strongest_negative(

        news: List[NewsResult],

    ) -> Optional[NewsResult]:

        negative = [

            x

            for x in news

            if x.sentiment.upper()

            == "NEGATIVE"

        ]

        if not negative:

            return None

        return min(

            negative,

            key=lambda x: x.score,

        )


# ============================================================
# SYMBOL SUMMARY
# ============================================================


def symbol_summary(

    symbol: str,

) -> Dict[str, Any]:

    news = get_news(symbol)

    stats = NewsStatistics.summary(news)

    return {

        "symbol": symbol,

        "news_count": len(news),

        "average_score": NewsMetrics.average_score(news),

        "best_news": NewsMetrics.strongest_positive(news),

        "worst_news": NewsMetrics.strongest_negative(news),

        "statistics": stats,

        "top_keywords": TrendEngine.keywords(news, 10),

    }


# ============================================================
# DASHBOARD WIDGET DATA
# ============================================================


def dashboard_widget(

    symbol: str,

) -> Dict[str, Any]:

    news = get_news(symbol)

    return {

        "headline_count": len(news),

        "average_score": NewsMetrics.average_score(news),

        "positive":

            len(

                NewsFilter.sentiment(

                    news,

                    "POSITIVE",

                )

            ),

        "negative":

            len(

                NewsFilter.sentiment(

                    news,

                    "NEGATIVE",

                )

            ),

        "neutral":

            len(

                NewsFilter.sentiment(

                    news,

                    "NEUTRAL",

                )

            ),

        "top5":

            NewsExporter.to_dict(

                news[:5]

            ),

    }

def calculate_statistics(items):

    total = len(items)

    positive = 0
    negative = 0
    neutral = 0

    scores = []
    categories = {}


    for item in items:


        # NewsResult nesnesi ise
        sentiment = getattr(
            item,
            "sentiment",
            None
        )

        score = getattr(
            item,
            "score",
            None
        )

        category = getattr(
            item,
            "category",
            None
        )


        # Dict ise
        if isinstance(item, dict):

            sentiment = item.get(
                "sentiment",
                sentiment
            )

            score = item.get(
                "score",
                score
            )

            category = item.get(
                "category",
                category
            )


        sentiment = str(
            sentiment or "NEUTRAL"
        ).upper()



        if sentiment == "POSITIVE":

            positive += 1


        elif sentiment == "NEGATIVE":

            negative += 1


        else:

            neutral += 1



        try:

            scores.append(
                float(score)
            )

        except:

            scores.append(50)



        category = category or "OTHER"


        categories[category] = (
            categories.get(category,0)+1
        )



    return {

        "total": total,

        "positive": positive,

        "negative": negative,

        "neutral": neutral,

        "average_score":
            round(
                sum(scores)/len(scores),
                2
            ) if scores else 50,

        "categories": categories

    }
# ============================================================
# END OF FILE
# ============================================================
def news_dashboard(symbol: str):

    items = get_news(
        symbol.upper()
    )

    return {
        "symbol": symbol.upper(),
        "news": [
            asdict(item)
            for item in items
        ],
        "statistics": calculate_statistics(items),
        "generated_at": datetime.utcnow().isoformat()
    }