"""
Weighted AI Decision Engine
BIST AI LAB v10.0
"""

from __future__ import annotations


class DecisionEngine:

    WEIGHTS = {

        "ml": 0.30,

        "technical": 0.20,

        "news": 0.20,

        "research": 0.15,

        "kap": 0.10,

        "risk": 0.05,

    }

    # =====================================================

    @staticmethod
    def _decision(score: float):

        if score >= 85:

            return "STRONG BUY"

        if score >= 70:

            return "BUY"

        if score >= 55:

            return "HOLD"

        if score >= 40:

            return "SELL"

        return "STRONG SELL"

    # =====================================================

    def evaluate(

        self,

        ml_score,

        technical_score,

        news_score,

        kap_score,

        research_score,

        risk_score,

    ):

        risk_component = max(

            0,

            min(

                100,

                100 - risk_score,

            ),

        )

        ai_score = (

            ml_score * self.WEIGHTS["ml"]

            + technical_score * self.WEIGHTS["technical"]

            + news_score * self.WEIGHTS["news"]

            + research_score * self.WEIGHTS["research"]

            + kap_score * self.WEIGHTS["kap"]

            + risk_component * self.WEIGHTS["risk"]

        )

        ai_score = round(

            ai_score,

            2,

        )

        decision = self._decision(ai_score)

        strengths = []

        weaknesses = []

        explanations = []

        modules = {

            "ML": ml_score,

            "Technical": technical_score,

            "News": news_score,

            "Research": research_score,

            "KAP": kap_score,

            "Risk": risk_component,

        }

        for module, score in modules.items():

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

        confidence = max(

            50,

            min(

                99,

                round(

                    ai_score

                    + len(strengths) * 2

                    - len(weaknesses),

                    1,

                ),

            ),

        )

        return {

            "decision": decision,

            "ai_score": ai_score,

            "confidence": confidence,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "explanations": explanations,

            "components": {

                "ml": round(ml_score, 2),

                "technical": round(technical_score, 2),

                "news": round(news_score, 2),

                "research": round(research_score, 2),

                "kap": round(kap_score, 2),

                "risk": round(risk_score, 2),

            },

            "weights": self.WEIGHTS,

        }