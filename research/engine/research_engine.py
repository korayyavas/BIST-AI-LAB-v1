"""
Research Engine
BIST AI LAB v7
"""

from __future__ import annotations

from research.classifier.report_classifier import ReportClassifier
from research.analyzer.daily_bulletin_analyzer import DailyBulletinAnalyzer
from research.analyzer.company_report_analyzer import CompanyReportAnalyzer


class ResearchEngine:

    def __init__(self):

        self.classifier = ReportClassifier()

        self.daily = DailyBulletinAnalyzer()

        self.company = CompanyReportAnalyzer()

    def analyze(self, text):

        report_type = self.classifier.classify(text)

        if report_type == "COMPANY_REPORT":

            result = self.company.analyze(text)

        elif report_type == "DAILY_BULLETIN":

            result = self.daily.analyze(text)

        else:

            result = {
                "report_type": "UNKNOWN",
                "summary": ""
            }

        result["report_type"] = report_type

        return result