from research.models.research_model import ResearchReport
from research.analyzer.research_analyzer import ResearchAnalyzer

report = ResearchReport(

    institution="Garanti BBVA",

    symbol="ASELS.IS",

    title="ASELSAN Research",

    summary="Strong export growth and new NATO contracts.",

    recommendation="BUY",

    target_price=520,

    analyst="AI",

    report_date="2026-07-19",

    confidence=93,

    url="https://example.com"

)

result = ResearchAnalyzer().analyze(report)

print(result)