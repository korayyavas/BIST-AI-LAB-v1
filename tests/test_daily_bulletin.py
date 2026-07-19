from research.parser.pdf_parser import PdfParser
from research.analyzer.daily_bulletin_analyzer import DailyBulletinAnalyzer

pdf = PdfParser()

text = pdf.parse("reports/sample_report.pdf")

ai = DailyBulletinAnalyzer()

result = ai.analyze(text)

print(result)