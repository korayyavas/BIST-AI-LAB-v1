from research.parser.pdf_parser import PdfParser
from research.analyzer.company_report_analyzer import CompanyReportAnalyzer

pdf = PdfParser()

text = pdf.parse("reports/company_report.pdf")

ai = CompanyReportAnalyzer()

result = ai.analyze(text)

print(result)