from research.classifier.report_classifier import ReportClassifier
from research.analyzer.daily_bulletin_analyzer import DailyBulletinAnalyzer
from research.analyzer.company_report_analyzer import CompanyReportAnalyzer
from research.analyzer.strategy_report_analyzer import StrategyReportAnalyzer


class ResearchEngine:

    def __init__(self):

        self.classifier = ReportClassifier()

        self.daily = DailyBulletinAnalyzer()
        self.company = CompanyReportAnalyzer()
        self.strategy = StrategyReportAnalyzer()

    def analyze(self, text):

        report_type = self.classifier.classify(text)

        if report_type == "DAILY_BULLETIN":
            return self.daily.analyze(text)

        if report_type == "COMPANY_REPORT":
            return self.company.analyze(text)

        if report_type == "STRATEGY_REPORT":
            return self.strategy.analyze(text)

        return {
            "report_type": report_type,
            "summary": "Unknown report type"
        }