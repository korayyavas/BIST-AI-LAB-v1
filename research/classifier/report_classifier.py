from core.llm_engine import LLMEngine


class ReportClassifier:

    def __init__(self):
        self.ai = LLMEngine()

    def classify(self, text: str):

        prompt = f"""
You are a financial document classifier.

Choose ONLY one type.

Return ONLY one word.

Types:

DAILY_BULLETIN
COMPANY_REPORT
STRATEGY_REPORT
SECTOR_REPORT
MACRO_REPORT

Document:

{text[:6000]}
"""

        result = self.ai.ask(prompt)

        return result.strip().upper()