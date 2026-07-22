"""
AI Intelligence Dashboard
BIST AI LAB v10.0 Professional
"""

from __future__ import annotations

from core.cache_manager import CacheManager


class IntelligenceDashboard:

    def __init__(

        self,

        symbol_service,

        decision_engine,

    ):

        self.symbol_service = symbol_service

        self.decision_engine = decision_engine

        self.cache = CacheManager()

    # =====================================================

    def analyze(self, symbol: str):

        symbol = symbol.upper()

        def producer():

            context = self.symbol_service.analyze(symbol)

            decision = self.decision_engine.evaluate(

                ml_score=context.ml_score,

                technical_score=context.technical_score,

                news_score=context.news_score,

                kap_score=context.kap_score,

                research_score=context.research_score,

                risk_score=context.risk_score,

            )

            consensus = context.consensus or {}

            explanation = []

            if context.ml_score >= 70:

                explanation.append(
                    "ML modeli pozitif sinyal üretiyor."
                )

            elif context.ml_score <= 40:

                explanation.append(
                    "ML modeli zayıf görünüm gösteriyor."
                )

            if context.technical_score >= 70:

                explanation.append(
                    "Teknik görünüm güçlü."
                )

            elif context.technical_score <= 40:

                explanation.append(
                    "Teknik görünüm zayıf."
                )

            if context.news_score >= 70:

                explanation.append(
                    "Haber akışı olumlu."
                )

            elif context.news_score <= 40:

                explanation.append(
                    "Haber akışı olumsuz."
                )

            if context.kap_score >= 70:

                explanation.append(
                    "KAP açıklamaları destekleyici."
                )

            if context.research_score >= 70:

                explanation.append(
                    "Araştırma raporları olumlu."
                )

            if context.risk_score <= 30:

                risk = "LOW"

            elif context.risk_score <= 60:

                risk = "MEDIUM"

            else:

                risk = "HIGH"

            return {

                "symbol": symbol,

                "decision": decision["decision"],

                "ai_score": round(

                    decision["ai_score"],

                    2,

                ),

                "confidence": decision.get(

                    "confidence",

                    85,

                ),

                "ml_score": round(

                    context.ml_score,

                    2,

                ),

                "technical_score": round(

                    context.technical_score,

                    2,

                ),

                "news_score": round(

                    context.news_score,

                    2,

                ),

                "kap_score": round(

                    context.kap_score,

                    2,

                ),

                "research_score": round(

                    context.research_score,

                    2,

                ),

                "consensus": consensus.get(

                    "market_view",

                    consensus.get(

                        "consensus",

                        "NOTR",

                    ),

                ),

                "consensus_score": consensus.get(

                    "score",

                    50,

                ),

                "consensus_summary": consensus.get(

                    "summary",

                    "",

                ),

                "target_price": consensus.get(

                    "average_target_price",

                ),

                "risk": risk,

                "summary": " ".join(explanation),

                "explanations": explanation,

                "strengths": consensus.get(

                    "strengths",

                    [],

                ),

                "risks": consensus.get(

                    "risks",

                    [],

                ),

                "sources": {

                    "news": len(context.news),

                    "kap": len(context.kap),

                    "research": len(context.research),

                },

            }

        return self.cache.get(

            f"dashboard_{symbol}",

            producer,

        )