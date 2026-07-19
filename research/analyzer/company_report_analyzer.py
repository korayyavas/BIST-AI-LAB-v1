import json

from core.llm_engine import LLMEngine


class CompanyReportAnalyzer:

    def __init__(self):
        self.ai = LLMEngine()

    def analyze(self, text):

        prompt = f"""
You are a senior equity research analyst.

Analyze this COMPANY research report.

Return ONLY valid JSON.

Schema:

{{
    "report_type":"COMPANY_REPORT",
    "company":"",
    "symbol":"",
    "recommendation":"BUY|HOLD|SELL",
    "target_price":0,
    "current_price":0,
    "upside_percent":0,
    "strengths":[],
    "risks":[],
    "financials":{{
        "revenue":"POSITIVE|NEUTRAL|NEGATIVE",
        "ebitda":"POSITIVE|NEUTRAL|NEGATIVE",
        "net_profit":"POSITIVE|NEUTRAL|NEGATIVE"
    }},
    "valuation":"",
    "confidence":0,
    "summary":""
}}

Never add extra fields.

Document:

{text[:12000]}
"""

        result = self.ai.ask(prompt)

        return json.loads(result)