"""
AI News Consensus Service
BIST AI LAB v10.0
Offline AI (Ollama + Gemma3)
"""

from __future__ import annotations

import json

from services.news_service import NewsService
from services.ollama_service import OllamaService


class NewsConsensusService:

    def __init__(self):

        self.news_service = NewsService()

        self.ai = OllamaService()

    # ======================================================

    def analyze(self, symbol: str):

        news = self.news_service.get_news(symbol)

        if not news:

            return {

                "summary": "Bugün haber bulunamadı.",

                "market_view": "NOTR",

                "importance": 1,

                "score": 50,

                "top_story": "",

                "positive": 0,

                "neutral": 0,

                "negative": 0,

                "strengths": [],

                "risks": [],

            }

        headlines = []

        positive = 0
        neutral = 0
        negative = 0

        for item in news:

            headlines.append(

                f"- {item.title_tr}"

            )

            if item.sentiment == "POSITIVE":

                positive += 1

            elif item.sentiment == "NEGATIVE":

                negative += 1

            else:

                neutral += 1

        prompt = f"""
Sen kıdemli bir portföy yöneticisisin.

Aşağıdaki haberleri birlikte analiz et.

Kurallar

- Türkçe yaz.
- Sadece JSON döndür.
- Markdown kullanma.
- Yatırım tavsiyesi verme.
- Haberlerin genel etkisini değerlendir.

JSON

{{
"summary":"",
"market_view":"POZITIF",
"importance":3,
"score":75,
"top_story":"",
"strengths":[
"",
""
],
"risks":[
"",
""
]
}}

market_view

POZITIF
NOTR
NEGATIF

importance

1
2
3
4
5

Haberler

{chr(10).join(headlines)}
"""

        try:

            content = self.ai.ask(prompt).strip()

            if content.startswith("```"):

                content = (

                    content
                    .replace("```json", "")
                    .replace("```JSON", "")
                    .replace("```", "")
                    .strip()

                )

            result = json.loads(content)

        except Exception:

            result = {

                "summary": "AI haber analizi oluşturulamadı.",

                "market_view": "NOTR",

                "importance": 3,

                "score": 50,

                "top_story": headlines[0],

                "strengths": [],

                "risks": [],

            }

        effect = str(

            result.get(

                "market_view",

                "NOTR",

            )

        ).upper()

        mapping = {

            "POSITIVE": "POZITIF",

            "NEGATIVE": "NEGATIF",

            "NEUTRAL": "NOTR",

            "POZITIF": "POZITIF",

            "NEGATIF": "NEGATIF",

            "NOTR": "NOTR",

        }

        result["market_view"] = mapping.get(

            effect,

            "NOTR",

        )

        result["importance"] = int(

            result.get(

                "importance",

                3,

            )

        )

        result["score"] = float(

            result.get(

                "score",

                50,

            )

        )

        result["positive"] = positive

        result["neutral"] = neutral

        result["negative"] = negative

        result["strengths"] = result.get(

            "strengths",

            [],

        )

        result["risks"] = result.get(

            "risks",

            [],

        )

        return result