import json

from core.llm_engine import LLMEngine


class LLMResearchAnalyzer:

    def __init__(self):
        self.ai = LLMEngine()

    def analyze(self, text: str):

        prompt = f"""
You are a financial analyst.

Analyze the following research report.

Return ONLY valid JSON.

No markdown.
No explanation.
No code block.

JSON schema:

{{
  "summary": "",
  "recommendation": "",
  "target_price": null,
  "risks": [],
  "opportunities": [],
  "confidence": 0
}}

Research Report:

{text[:10000]}
"""

        result = self.ai.ask(prompt).strip()

        print("\n========== LLM RESPONSE ==========\n")
        print(result)
        print("\n==================================\n")

        start = result.find("{")
        end = result.rfind("}")

        if start == -1 or end == -1:
            raise RuntimeError("LLM did not return JSON.")

        result = result[start:end + 1]

        return json.loads(result)