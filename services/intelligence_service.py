from services.news_service import NewsService
from services.kap_service import KapService


class IntelligenceService:

    def __init__(self):
        self.news = NewsService()
        self.kap = KapService()

    def analyze(self, symbol):

        news = self.news.get_news(symbol)
        kap = self.kap.get_events(symbol)

        news_score = (
            sum(x.score for x in news) / len(news)
            if news else 0
        )

        kap_score = (
            sum(x.score for x in kap) / len(kap)
            if kap else 0
        )

        return {
            "news": news,
            "kap": kap,
            "news_score": round(news_score, 2),
            "kap_score": round(kap_score, 2),
        }