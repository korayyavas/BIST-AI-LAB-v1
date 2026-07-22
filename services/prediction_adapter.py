"""
Prediction Adapter
BIST AI LAB v6

Connects:
Market Data
Feature Pipeline
Prediction Service
Dashboard
"""

import logging

from pipeline.feature_pipeline import FeaturePipeline
from services.prediction_service import PredictionService
from services.providers.market_data_provider import market_data_provider


logger = logging.getLogger(__name__)


class PredictionAdapter:


    def __init__(self):

        self.pipeline = FeaturePipeline()

        self.service = PredictionService()



    def predict(self, symbol: str):

        symbol = symbol.upper()


        try:

            logger.info(
                "ML prediction started: %s",
                symbol
            )


            # -----------------------------
            # MARKET DATA
            # -----------------------------

            df = market_data_provider.get(
                symbol
            )


            if df is None or df.empty:

                raise ValueError(
                    "Market data empty"
                )


            # -----------------------------
            # FEATURE ENGINEERING
            # -----------------------------

            processed = self.pipeline.transform(
                df
            )


            features = self.pipeline.latest_features(
                processed
            )


            # -----------------------------
            # CURRENT PRICE
            # -----------------------------

            current_price = float(
                df["Close"].iloc[-1]
            )


            atr = 0.0

            if "ATR" in processed.columns:

                atr = float(
                    processed["ATR"].iloc[-1]
                )


            # -----------------------------
            # MODEL
            # -----------------------------

            result = self.service.predict(

                features=features,

                current_price=current_price,

                atr=atr

            )


            return {

                "symbol": symbol,

                "price": current_price,

                **result

            }


        except Exception as e:


            logger.error(
                "Prediction failed %s: %s",
                symbol,
                e
            )


            return {

                "symbol": symbol,

                "status": "error",

                "message": str(e)

            }



prediction_adapter = PredictionAdapter()