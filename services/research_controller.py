"""
Research Controller
BIST AI LAB v7
"""

from services.research_service import ResearchService


class ResearchController:

    def __init__(self):

        self.service = ResearchService()

    def analyze(self, symbol: str):

        return self.service.get_reports(symbol)