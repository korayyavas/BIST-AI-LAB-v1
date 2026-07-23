"""
Prediction Adapter
BIST AI LAB v6

Market
Feature Pipeline
ML Model
Cache
Dashboard
"""

import logging


from pipeline.feature_pipeline import FeaturePipeline

from services.prediction_service import PredictionService

from services.providers.market_data_provider import (
    market_data_provider
)

from services.cache.prediction_cache import (
    prediction_cache
)



logger = logging.getLogger(__name__)



class PredictionAdapter:



    def __init__(self):

        self.pipeline = FeaturePipeline()

        self.service = PredictionService()



    def predict(
        self,
        symbol: str
    ):


        symbol = symbol.upper()



        cached = prediction_cache.get(
            symbol
        )


        if cached:


            logger.info(
                "Prediction cache hit: %s",
                symbol
            )


            return cached




        try:


            logger.info(
                "ML prediction started: %s",
                symbol
            )



            df = market_data_provider.get(
                symbol
            )



            if df is None or df.empty:

                raise ValueError(
                    "Market data empty"
                )



            processed = self.pipeline.transform(
                df
            )



            features = self.pipeline.latest_features(
                processed
            )



            current_price = float(

                df["Close"].iloc[-1]

            )



            atr = 0.0


            if "ATR" in processed.columns:

                atr = float(

                    processed["ATR"].iloc[-1]

                )




            result = self.service.predict(

                features=features,

                current_price=current_price,

                atr=atr

            )




            response = {


                "symbol": symbol,


                "price": current_price,


                **result


            }



            prediction_cache.set(

                symbol,

                response

            )



            logger.info(

                "ML prediction completed: %s",

                response

            )



            return response




        except Exception as e:


            logger.error(

                "Prediction failed %s: %s",

                symbol,

                e

            )



            return {


                "symbol": symbol,


                "status":"error",


                "message":str(e)

            }





prediction_adapter = PredictionAdapter()



__all__=[

    "PredictionAdapter",

    "prediction_adapter"

]