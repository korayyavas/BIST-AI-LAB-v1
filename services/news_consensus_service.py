"""
AI News Consensus Service
BIST AI LAB v9
"""

from __future__ import annotations

import json

from openai import OpenAI

from config.settings import OPENAI_API_KEY
from services.news_service import NewsService


class NewsConsensusService:

    def __init__(self):

        self.news_service = NewsService()

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    # ======================================================

    def analyze(self, symbol: str):

        news = self.news_service.get_news(symbol)

        if len(news) == 0:

            return {

                "summary": "Bugün haber bulunamadı.",

                "market_view": "NOTR",

                "importance": 1,

                "score": 50,

                "top_story": "",

                "positive": 0,

                "neutral": 0,

                "negative": 0,

            }

        headlines = []

        positive = 0
        neutral = 0
        negative = 0

        for item in news:

            headlines.append(item.title_tr)

            if item.sentiment == "POSITIVE":
                positive += 1

            elif item.sentiment == "NEGATIVE":
                negative += 1

            else:
                neutral += 1

        prompt = f"""
Sen kıdemli bir finans analistisisin.

Aşağıdaki haberleri birlikte değerlendir.

Yatırım tavsiyesi verme.

JSON dışında hiçbir şey yazma.

JSON formatı

{{
"summary":"",
"market_view":"",
"importance":0,
"score":0,
"top_story":""
}}

market_view

POZITIF
NOTR
NEGATIF

importance

1-5

score

0-100

Haberler

{chr(10).join(headlines)}
"""

        try:

            response = self.client.chat.completions.create(

                model="gpt-4.1-mini",

                temperature=0.2,

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            result = json.loads(
                response.choices[0].message.content
            )

        except Exception:

            result = {

                "summary": "AI analizine ulaşılamadı.",

                "market_view": "NOTR",

                "importance": 3,

                "score": 50,

                "top_story": headlines[0],

            }

        result["positive"] = positive
        result["neutral"] = neutral
        result["negative"] = negative

        return result