"""
AI News Intelligence Service
BIST AI LAB v9
"""

from __future__ import annotations

import json

from openai import OpenAI

from config.settings import OPENAI_API_KEY


class NewsAIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    # =====================================================

    def analyze(self, title: str):

        prompt = f"""
Sen kıdemli bir finans analistisisin.

Görevlerin:

1. Haberi Türkçeye çevir.
2. En fazla iki cümlelik özet oluştur.
3. Piyasa etkisini belirle.
4. Haber önem derecesini belirle.
5. Kısa AI yorumu oluştur.

Yatırım tavsiyesi verme.

Sadece JSON döndür.

JSON formatı

{{
"title_tr":"",
"summary":"",
"market_effect":"",
"importance":0,
"ai_comment":""
}}

Kurallar

market_effect

POZITIF
NOTR
NEGATIF

importance

1-5

Haber

{title}
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

            content = response.choices[0].message.content.strip()

            if content.startswith("```"):

                content = (
                    content.replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            result = json.loads(content)

            return {

                "title_tr": result.get(
                    "title_tr",
                    title,
                ),

                "summary": result.get(
                    "summary",
                    "",
                ),

                "market_effect": result.get(
                    "market_effect",
                    "NOTR",
                ),

                "importance": int(
                    result.get(
                        "importance",
                        3,
                    )
                ),

                "ai_comment": result.get(
                    "ai_comment",
                    "",
                ),

            }

        except Exception as e:

            print("=" * 80)
            print("AI NEWS ERROR")
            print(e)
            print("=" * 80)

            return {

                "title_tr": title,

                "summary": "",

                "market_effect": "NOTR",

                "importance": 3,

                "ai_comment": "",

            }