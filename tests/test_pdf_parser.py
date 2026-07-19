from research.parser.pdf_parser import PdfParser

parser = PdfParser()

text = parser.parse("reports/sample_report.pdf")

print(text[:3000])