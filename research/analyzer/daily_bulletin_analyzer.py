import json

from core.llm_engine import LLMEngine


class DailyBulletinAnalyzer:

    def __init__(self):
        self.ai = LLMEngine()

    def analyze(self, text):

        prompt = f"""
You are a senior financial analyst.

Analyze this DAILY market bulletin.

Return ONLY valid JSON.

Use EXACTLY this schema.

{{
    "report_type":"DAILY_BULLETIN",
    "market_sentiment":"POSITIVE|NEUTRAL|NEGATIVE",
    "bist_outlook":"BULLISH|SIDEWAYS|BEARISH",
    "macro_risk":"LOW|MEDIUM|HIGH",
    "important_events":[
        "..."
    ],
    "watchlist":[
        "..."
    ],
    "summary":"..."
}}

Never invent new fields.

Never rename fields.

Never explain.

Document:

{text[:10000]}
"""

        result = self.ai.ask(prompt)

        return json.loads(result)