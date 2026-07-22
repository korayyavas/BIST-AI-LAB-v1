"""
BIST AI LAB Intelligence Engine v10.0
"""

from __future__ import annotations

from typing import Any


class IntelligenceEngine:

    WEIGHTS = {
        "prediction": 0.25,
        "technical": 0.20,
        "news": 0.20,
        "research": 0.15,
        "kap": 0.10,
        "risk": 0.10,
    }

    def __init__(self):
        pass

    # =========================================================

    def _score(self, obj: Any, default: float = 50.0) -> float:

        if obj is None:
            return default

        if isinstance(obj, (int, float)):
            return float(obj)

        if isinstance(obj, dict):

            for key in (
                "score",
                "confidence",
                "risk_score",
                "technical_score",
                "news_score",
            ):

                if key in obj:

                    try:
                        return float(obj[key])
                    except Exception:
                        pass

        return default

    # =========================================================

    def _recommendation(self, score: float):

        if score >= 85:
            return "STRONG BUY"

        if score >= 70:
            return "BUY"

        if score >= 55:
            return "HOLD"

        if score >= 40:
            return "SELL"

        return "STRONG SELL"

    # =========================================================

    def analyze(
        self,
        prediction,
        technical,
        news,
        research,
        kap,
        risk,
    ):

        prediction_score = self._score(prediction)

        technical_score = self._score(technical)

        news_score = self._score(news)

        research_score = self._score(research)

        kap_score = self._score(kap)

        risk_raw = self._score(risk)

        risk_score = max(0.0, min(100.0, 100.0 - risk_raw))

        components = {

            "Prediction": prediction_score,

            "Technical": technical_score,

            "News": news_score,

            "Research": research_score,

            "KAP": kap_score,

            "Risk": risk_score,

        }

        final_score = round(

            prediction_score * self.WEIGHTS["prediction"]

            + technical_score * self.WEIGHTS["technical"]

            + news_score * self.WEIGHTS["news"]

            + research_score * self.WEIGHTS["research"]

            + kap_score * self.WEIGHTS["kap"]

            + risk_score * self.WEIGHTS["risk"],

            2,

        )

        recommendation = self._recommendation(final_score)

        strengths = []

        weaknesses = []

        explanations = []

        for module, score in components.items():

            if score >= 80:

                strengths.append(module)

                explanations.append(

                    f"{module} çok güçlü."

                )

            elif score >= 65:

                strengths.append(module)

                explanations.append(

                    f"{module} olumlu."

                )

            elif score <= 35:

                weaknesses.append(module)

                explanations.append(

                    f"{module} ciddi risk oluşturuyor."

                )

            elif score <= 50:

                weaknesses.append(module)

                explanations.append(

                    f"{module} zayıf."

                )

        confidence = round(

            min(

                100,

                60

                + len(strengths) * 6

                - len(weaknesses) * 4,

            ),

            1,

        )

        return {

            "score": final_score,

            "recommendation": recommendation,

            "confidence": confidence,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "explanations": explanations,

            "module_scores": {

                "prediction": prediction_score,

                "technical": technical_score,

                "news": news_score,

                "research": research_score,

                "kap": kap_score,

                "risk": risk_score,

            },

            "components": {

                "prediction": prediction,

                "technical": technical,

                "news": news,

                "research": research,

                "kap": kap,

                "risk": risk,

            },

        }