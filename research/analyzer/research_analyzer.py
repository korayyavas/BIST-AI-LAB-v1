from research.models.research_model import ResearchReport


class ResearchAnalyzer:

    def analyze(self, report: ResearchReport):

        score = 50

        recommendation = report.recommendation.upper()

        if recommendation == "BUY":
            score = 90

        elif recommendation == "OUTPERFORM":
            score = 80

        elif recommendation == "HOLD":
            score = 60

        elif recommendation == "UNDERPERFORM":
            score = 35

        elif recommendation == "SELL":
            score = 15

        return {

            "institution": report.institution,

            "recommendation": recommendation,

            "target_price": report.target_price,

            "confidence": report.confidence,

            "score": score,

            "summary": report.summary,

            "url": report.url

        }