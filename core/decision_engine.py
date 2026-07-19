class DecisionEngine:

    def evaluate(
        self,
        ml_score,
        technical_score,
        news_score,
        kap_score,
        research_score,
        risk_score,
    ):

        weights = {
            "ml": 0.30,
            "technical": 0.20,
            "research": 0.20,
            "news": 0.10,
            "kap": 0.10,
            "risk": 0.10,
        }

        risk_component = 100 - risk_score

        final_score = (
            ml_score * weights["ml"]
            + technical_score * weights["technical"]
            + research_score * weights["research"]
            + news_score * weights["news"]
            + kap_score * weights["kap"]
            + risk_component * weights["risk"]
        )

        final_score = round(final_score, 2)

        if final_score >= 85:
            decision = "STRONG BUY"

        elif final_score >= 70:
            decision = "BUY"

        elif final_score >= 55:
            decision = "HOLD"

        elif final_score >= 40:
            decision = "SELL"

        else:
            decision = "STRONG SELL"

        return {
            "decision": decision,
            "ai_score": final_score,
            "components": {
                "ml": ml_score,
                "technical": technical_score,
                "research": research_score,
                "news": news_score,
                "kap": kap_score,
                "risk": risk_score,
            },
        }