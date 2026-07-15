"""
API Routes
BIST AI LAB v3
"""

from __future__ import annotations

from fastapi import APIRouter

from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from services.prediction_service import PredictionService


router = APIRouter()

provider = YahooFinanceProvider()

pipeline = FeaturePipeline()

prediction = PredictionService()


# ==================================================

@router.get("/")

def home():

    return {

        "project": "BIST AI LAB",

        "version": "3.0.0",

        "status": "running",

    }


# ==================================================

@router.get("/predict/{ticker}")

def predict(ticker: str):

    ticker = ticker.upper()

    if not ticker.endswith(".IS"):

        ticker += ".IS"

    df = provider.download(ticker)

    df = pipeline.transform(df)

    X = pipeline.latest_features(df)

    current_price = float(df.iloc[-1]["Close"])

    atr = float(df.iloc[-1]["ATR"])

    result = prediction.predict(

        current_price=current_price,

        features=X,

        atr=atr,

    )

    result["ticker"] = ticker

    return result