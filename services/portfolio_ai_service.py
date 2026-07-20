"""
Portfolio AI Service
BIST AI LAB v8
"""

from __future__ import annotations

from services.intelligence_dashboard import IntelligenceDashboard


class PortfolioAIService:

    def __init__(self, dashboard: IntelligenceDashboard):

        self.dashboard = dashboard

    def build(self, symbols):

        portfolio = []

        for symbol in symbols:

            try:

                result = self.dashboard.analyze(symbol)

                portfolio.append(result)

            except Exception as e:

                print(symbol, e)

        portfolio.sort(

            key=lambda x: x["ai_score"],

            reverse=True,

        )

        return portfolio