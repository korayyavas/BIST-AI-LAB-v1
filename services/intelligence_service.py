"""
BIST AI LAB Intelligence Service v10.0
"""

from __future__ import annotations

from core.intelligence_engine import IntelligenceEngine

from services.prediction_controller import PredictionController
from services.technical_score_service import TechnicalScoreService
from services.news_consensus_service import NewsConsensusService
from services.research_controller import ResearchController
from services.kap_service import KapService


class IntelligenceService:

    def __init__(self):

        self.engine = IntelligenceEngine()

        self.prediction = PredictionController()

        self.technical = TechnicalScoreService()

        self.news = NewsConsensusService()

        self.research = ResearchController()

        self.kap = KapService()

    # =========================================================

    def analyze(self, symbol: str):

        prediction = {
            "score": 50,
        }

        technical = {
            "score": 50,
        }

        news = {
            "score": 50,
        }

        research = {
            "score": 50,
            "reports": [],
        }

        kap = {
            "score": 50,
            "events": [],
        }

        risk = {
            "risk_score": 50,
        }

        # =====================================================
        # Prediction
        # =====================================================

        try:

            prediction = self.prediction.predict(symbol)

            if prediction is None:
                prediction = {"score": 50}

        except Exception as e:

            prediction = {

                "score": 50,

                "error": str(e),

            }

        # =====================================================
        # Technical
        # =====================================================

        try:

            technical = self.technical.analyze(symbol)

            if technical is None:
                technical = {"score": 50}

        except Exception as e:

            technical = {

                "score": 50,

                "error": str(e),

            }

        # =====================================================
        # News
        # =====================================================

        try:

            news = self.news.analyze(symbol)

            if news is None:
                news = {"score": 50}

        except Exception as e:

            news = {

                "score": 50,

                "error": str(e),

            }

        # =====================================================
        # Research
        # =====================================================

        try:

            reports = self.research.analyze(symbol)

            if isinstance(reports, list):

                research = {

                    "score": 60 if len(reports) else 50,

                    "reports": reports,

                }

            elif isinstance(reports, dict):

                research = reports

            else:

                research = {

                    "score": 50,

                    "reports": [],

                }

        except Exception as e:

            research = {

                "score": 50,

                "reports": [],

                "error": str(e),

            }

        # =====================================================
        # KAP
        # =====================================================

        try:

            events = self.kap.get_announcements(symbol)

            kap = {

                "score": 60 if len(events) else 50,

                "events": events,

            }

        except Exception as e:

            kap = {

                "score": 50,

                "events": [],

                "error": str(e),

            }

        # =====================================================
        # Risk
        # =====================================================

        risk = {

            "risk_score": 50,

        }

        # =====================================================
        # Intelligence Engine
        # =====================================================

        result = self.engine.analyze(

            prediction=prediction,

            technical=technical,

            news=news,

            research=research,

            kap=kap,

            risk=risk,

        )

        result["symbol"] = symbol.upper()

        return result