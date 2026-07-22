"""
AI News Intelligence Service
BIST AI LAB v10
"""

from __future__ import annotations

import json

from services.ollama_service import OllamaService


class NewsAIService:

    def __init__(self):

        self.ollama = OllamaService()

    # =====================================================

    def analyze(self, headlines: list[str]):

        if not headlines:

            return []

        prompt = f"""
Sen 20 yıllık deneyime sahip kıdemli bir finans analisti ve ekonomi editörüsün.

Aşağıdaki haber başlıklarını analiz et.

Her haber için yalnızca JSON üret.

Açıklama yazma.
Markdown kullanma.
Kod bloğu kullanma.

JSON formatı:

[
  {{
    "title_tr":"",
    "summary":"",
    "market_effect":"POZITIF",
    "importance":3,
    "ai_comment":""
  }}
]

market_effect sadece:

POZITIF
NOTR
NEGATIF

importance:

1
2
3
4
5

Haberler:

{chr(10).join(f"- {x}" for x in headlines)}
"""

        content = self.ollama.ask(prompt)

        content = content.strip()

        if content.startswith("```"):

            content = (
                content
                .replace("```json", "")
                .replace("```JSON", "")
                .replace("```", "")
                .strip()
            )

        try:

            result = json.loads(content)

            if isinstance(result, list):

                return result

        except Exception:

            pass

        return []