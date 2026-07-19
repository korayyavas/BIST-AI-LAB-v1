from research.parser.pdf_parser import PdfParser
from research.analyzer.report_summarizer import ReportSummarizer

pdf = PdfParser()

text = pdf.parse("reports/sample_report.pdf")

ai = ReportSummarizer()

summary = ai.summarize(text)

print(summary)