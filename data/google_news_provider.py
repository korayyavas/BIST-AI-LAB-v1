import requests

from config.settings import NEWS_API_KEY
from data.news_provider import NewsProvider


class GoogleNewsProvider(NewsProvider):

    def search(self, keyword: str):

        url = "https://newsapi.org/v2/everything"

        response = requests.get(
            url,
            params={
                "q": keyword,
                "language": "en",
                "sortBy": "publishedAt",
                "pageSize": 10,
                "apiKey": NEWS_API_KEY,
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("articles", [])