"""
Symbol Analysis Service
BIST AI LAB v10.0 Intelligence Pipeline
"""

from __future__ import annotations

from statistics import mean

from models.intelligence_context import IntelligenceContext

from services.prediction_service import PredictionService
from services.technical_score_service import TechnicalScoreService

from data.yahoo_provider import YahooFinanceProvider

from pipeline.feature_pipeline import FeaturePipeline


class SymbolAnalysisService:

    def __init__(

        self,

        news_service,

        kap_service,

        research_service,

        consensus_engine,

    ):

        self.news_service = news_service

        self.kap_service = kap_service

        self.research_service = research_service

        self.consensus_engine = consensus_engine

        self.predictor = PredictionService()

        self.provider = YahooFinanceProvider()

        self.pipeline = FeaturePipeline()

        self.technical = TechnicalScoreService()

    # ======================================================

    def analyze(self, symbol: str):

        context = IntelligenceContext(symbol=symbol)

        ticker = symbol if symbol.endswith(".IS") else f"{symbol}.IS"

        # =====================================================
        # ML + TECHNICAL
        # =====================================================

        try:

            df = self.provider.download(ticker)

            df = self.pipeline.transform(df)

            features = df.select_dtypes(include=["number"]).tail(1)

            row = df.tail(1)

            atr = (

                float(row["ATR"].iloc[0])

                if "ATR" in row.columns

                else 0.0

            )

            prediction = self.predictor.predict(

                row,

                features,

                atr,

            )

            context.prediction = prediction

            context.ml_score = float(

                prediction.get(

                    "confidence",

                    50,

                )

            )

            context.technical_score = float(

                self.technical.calculate(

                    row.iloc[0]

                )

            )

        except Exception as e:

            print("ML ERROR:", e)

            context.ml_score = 50

            context.technical_score = 50

        # =====================================================
        # NEWS
        # =====================================================

        try:

            context.news = self.news_service.get_news(symbol)

            if context.news:

                context.news_score = round(

                    mean(

                        [

                            float(

                                getattr(

                                    x,

                                    "score",

                                    50,

                                )

                            )

                            for x in context.news

                        ]

                    ),

                    2,

                )

            else:

                context.news_score = 50

        except Exception as e:

            print("NEWS ERROR:", e)

            context.news = []

            context.news_score = 50

        # =====================================================
        # KAP
        # =====================================================

        try:

            context.kap = self.kap_service.get_announcements(symbol)

            if context.kap:

                scores = []

                for item in context.kap:

                    if hasattr(item, "score"):

                        scores.append(

                            float(item.score)

                        )

                    elif isinstance(item, dict):

                        scores.append(

                            float(

                                item.get(

                                    "score",

                                    50,

                                )

                            )

                        )

                context.kap_score = (

                    round(

                        mean(scores),

                        2,

                    )

                    if scores

                    else 50

                )

            else:

                context.kap_score = 50

        except Exception as e:

            print("KAP ERROR:", e)

            context.kap = []

            context.kap_score = 50

        # =====================================================
        # RESEARCH
        # =====================================================

        try:

            context.research = self.research_service.get_reports(symbol)

            if context.research:

                scores = [

                    float(

                        report.get(

                            "confidence",

                            50,

                        )

                    )

                    for report in context.research

                ]

                context.research_score = round(

                    mean(scores),

                    2,

                )

            else:

                context.research_score = 50

        except Exception as e:

            print("RESEARCH ERROR:", e)

            context.research = []

            context.research_score = 50

        # =====================================================
        # NEWS CONSENSUS
        # =====================================================

        try:

            context.consensus = self.consensus_engine.analyze(symbol)

        except Exception as e:

            print("CONSENSUS ERROR:", e)

            context.consensus = {

                "summary": "",

                "market_view": "NOTR",

                "score": 50,

            }

        # =====================================================
        # AI SCORE
        # =====================================================

        context.ai_score = round(

            (

                context.ml_score * 0.30

                + context.technical_score * 0.20

                + context.news_score * 0.20

                + context.research_score * 0.15

                + context.kap_score * 0.15

            ),

            2,

        )

        return context