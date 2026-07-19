from dataclasses import dataclass

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

    def get_news(self, symbol: str):

        keyword = SYMBOL_MAP.get(symbol, symbol)

        articles = self.provider.search(keyword)

        news = []

        for article in articles:

            title = article.get("title", "")

            analysis = self.sentiment.analyze(title)

            source = article.get("source", {})
            if isinstance(source, dict):
                source_name = source.get("name", "Unknown")
            else:
                source_name = "Unknown"

            news.append(
                NewsResult(
                    source=source_name,
                    title=title,
                    url=article.get("url", ""),
                    sentiment=analysis["sentiment"],
                    score=analysis["score"],
                )
            )

        return news