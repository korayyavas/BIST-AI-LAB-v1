from research.parser.pdf_parser import PdfParser
from research.classifier.report_classifier import ReportClassifier

pdf = PdfParser()

text = pdf.parse("reports/sample_report.pdf")

classifier = ReportClassifier()

print(classifier.classify(text))