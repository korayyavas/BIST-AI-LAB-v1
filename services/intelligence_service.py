"""
BIST AI LAB Intelligence Service v9
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

        prediction = {}

        technical = {}

        news = {}

        research = {}

        kap = {}

        risk = {
            "risk_score": 50,
        }

        # -----------------------------------------------------

        try:

            prediction = self.prediction.predict(symbol)

        except Exception as e:

            prediction = {
                "score": 50,
                "error": str(e),
            }

        # -----------------------------------------------------

        try:

            technical = self.technical.analyze(symbol)

        except Exception as e:

            technical = {
                "score": 50,
                "error": str(e),
            }

        # -----------------------------------------------------

        try:

            news = self.news.analyze(symbol)

        except Exception as e:

            news = {
                "score": 50,
                "error": str(e),
            }

        # -----------------------------------------------------

        try:

            research = self.research.analyze(symbol)

            if isinstance(research, list):

                research = {
                    "score": 60 if research else 50,
                    "reports": research,
                }

        except Exception as e:

            research = {
                "score": 50,
                "error": str(e),
            }

        # -----------------------------------------------------

        try:

            announcements = self.kap.get_announcements(symbol)

            kap = {

                "score": 60 if announcements else 50,

                "events": announcements,

            }

        except Exception as e:

            kap = {
                "score": 50,
                "error": str(e),
            }

        # -----------------------------------------------------



        # -----------------------------------------------------

        return self.engine.analyze(

            prediction=prediction,

            technical=technical,

            news=news,

            research=research,

            kap=kap,

            risk=risk,

        )