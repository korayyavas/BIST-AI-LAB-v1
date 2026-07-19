from research.parser.pdf_parser import PdfParser
from research.analyzer.llm_research_analyzer import LLMResearchAnalyzer

pdf = PdfParser()

text = pdf.parse("reports/sample_report.pdf")

ai = LLMResearchAnalyzer()

result = ai.analyze(text)

print(result)