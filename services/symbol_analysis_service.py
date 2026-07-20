"""
Symbol Analysis Service
BIST AI LAB v7
"""

from __future__ import annotations

from models.intelligence_context import IntelligenceContext

from services.prediction_service import PredictionService

from data.yahoo_provider import YahooFinanceProvider

from pipeline.feature_pipeline import FeaturePipeline

from services.technical_score_service import TechnicalScoreService


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
        self.technical = TechnicalScoreService()

        self.predictor = PredictionService()

        self.provider = YahooFinanceProvider()

        self.pipeline = FeaturePipeline()

    # ======================================================

    def analyze(self, symbol: str):

        context = IntelligenceContext(symbol=symbol)

        # -----------------------------
        # ML SCORE
        # -----------------------------

        try:

            ticker = symbol if symbol.endswith(".IS") else f"{symbol}.IS"

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

            context.technical_score = self.technical.calculate(
                row.iloc[0]
            )
            context.ml_score = float(
                prediction["confidence"]
            )

        except Exception as e:

            print("ML Score Error:", e)

                # -----------------------------
        # NEWS
        # -----------------------------

        try:

            ticker = symbol if symbol.endswith(".IS") else f"{symbol}.IS"

            context.news = self.news_service.get_news(ticker)

            if context.news:

                scores = []

                for item in context.news:

                    score = float(getattr(item, "score", 50))

                    sentiment = getattr(item, "sentiment", "NEUTRAL")

                    if sentiment == "POSITIVE":

                        scores.append(min(100, 50 + score / 2))

                    elif sentiment == "NEGATIVE":

                        scores.append(max(0, 50 - score / 2))

                    else:

                        scores.append(50)

                context.news_score = round(
                    sum(scores) / len(scores),
                    2,
                )

        except Exception as e:

            print("News Error:", e)

        
       

        # -----------------------------
        # KAP
        # -----------------------------

        try:

            context.kap = self.kap_service.get_announcements(symbol)

            if context.kap:

                scores = [
                    float(getattr(item, "score", 50))
                    for item in context.kap
                ]

                context.kap_score = round(
                    sum(scores) / len(scores),
                    2,
                )

        except Exception as e:

            print("KAP Error:", e)

        # RESEARCH
        # -----------------------------

        try:

            context.research = self.research_service.get_reports(symbol)

            if context.research:

                scores = [
                    float(r.get("confidence", 50))
                    for r in context.research
                ]

                context.research_score = round(
                    sum(scores) / len(scores),
                    2,
                )

        except Exception as e:

            print("Research Error:", e)    

        # -----------------------------
        # CONSENSUS
        # -----------------------------

        try:

            context.consensus = self.consensus_engine.analyze(
                context.research
            )

        except Exception as e:

            print("Consensus Error:", e)

        return context
