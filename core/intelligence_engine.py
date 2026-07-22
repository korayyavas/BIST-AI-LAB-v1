"""
BIST AI LAB Intelligence Engine v9
"""

from __future__ import annotations

from statistics import mean


class IntelligenceEngine:

    def __init__(self):
        pass

    def _safe_score(self, value, default=50):

        if value is None:
            return default

        if isinstance(value, dict):

            if "score" in value:
                return float(value["score"])

            if "confidence" in value:
                return float(value["confidence"])

        if isinstance(value, (int, float)):
            return float(value)

        return default

    def analyze(
        self,
        prediction,
        technical,
        news,
        research,
        kap,
        risk,
    ):

        prediction_score = self._safe_score(prediction)

        technical_score = self._safe_score(technical)

        news_score = self._safe_score(news)

        research_score = self._safe_score(research)

        kap_score = self._safe_score(kap)

        risk_score = 100 - self._safe_score(risk)

        final_score = round(
            mean(
                [
                    prediction_score,
                    technical_score,
                    news_score,
                    research_score,
                    kap_score,
                    risk_score,
                ]
            ),
            2,
        )

        if final_score >= 85:

            recommendation = "STRONG BUY"

        elif final_score >= 70:

            recommendation = "BUY"

        elif final_score >= 50:

            recommendation = "HOLD"

        elif final_score >= 30:

            recommendation = "SELL"

        else:

            recommendation = "STRONG SELL"

        strengths = []

        weaknesses = []

        modules = {

            "Prediction": prediction_score,
            "Technical": technical_score,
            "News": news_score,
            "Research": research_score,
            "KAP": kap_score,
            "Risk": risk_score,

        }

        for name, score in modules.items():

            if score >= 70:
                strengths.append(name)

            elif score <= 40:
                weaknesses.append(name)

        return {

            "score": final_score,

            "recommendation": recommendation,

            "confidence": final_score,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "components": {

                "prediction": prediction,

                "technical": technical,

                "news": news,

                "research": research,

                "kap": kap,

                "risk": risk,

            },

        }