"""
AI Intelligence Dashboard
BIST AI LAB v8
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

            return {

                "symbol": symbol,

                "decision": decision["decision"],

                "ai_score": decision["ai_score"],

                "confidence": 85,

                "ml_score": context.ml_score,

                "technical_score": context.technical_score,

                "research_score": context.research_score,

                "news_score": context.news_score,

                "kap_score": context.kap_score,

                "consensus": context.consensus.get(
                    "consensus",
                    "UNKNOWN",
                ),

                "target_price": context.consensus.get(
                    "average_target_price",
                ),

                "risk": (
                    "LOW"
                    if context.risk_score < 30
                    else "MEDIUM"
                ),

                "summary": "",

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