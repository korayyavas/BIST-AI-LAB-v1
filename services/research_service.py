"""
Research Service
BIST AI LAB v8
"""

from __future__ import annotations

from core.cache_manager import CacheManager

from research.providers.local_provider import LocalResearchProvider
from research.parser.document_loader import DocumentLoader
from research.engine.research_engine import ResearchEngine


class ResearchService:

    def __init__(self):

        self.provider = LocalResearchProvider()

        self.loader = DocumentLoader()

        self.engine = ResearchEngine()

        self.cache = CacheManager()

    def get_reports(self, symbol: str):

        def producer():

            reports = []

            files = self.provider.get_reports(symbol)

            for file in files:

                try:

                    text = self.loader.load(file["path"])

                    result = self.engine.analyze(text)

                    result.setdefault("recommendation", "HOLD")
                    result.setdefault("target_price", None)
                    result.setdefault("confidence", 50)
                    result.setdefault("summary", "")

                    result["broker"] = file["broker"]
                    result["title"] = file["title"]

                    reports.append(result)

                except Exception as e:

                    print(e)

            return reports

        return self.cache.get(
            f"research_{symbol}",
            producer,
        )