"""
AI Screener Service
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd

from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from services.prediction_service import PredictionService


class ScreenerService:

    def __init__(self):

        self.provider = YahooFinanceProvider()

        self.pipeline = FeaturePipeline()

        self.prediction = PredictionService()

    # ==================================================

    def scan(
        self,
        tickers: list[str],
    ) -> pd.DataFrame:

        rows = []

        for ticker in tickers:

            try:

                df = self.provider.download(
                    ticker
                )

                if df.empty:
                    continue

                df = self.pipeline.transform(
                    df
                )

                features = self.pipeline.latest_features(
                    df
                )

                current_price = float(
                    df.iloc[-1]["Close"]
                )

                atr = float(
                    df.iloc[-1]["ATR"]
                )

                result = self.prediction.predict(

                    current_price=current_price,

                    features=features,

                    atr=atr,

                )

                rows.append({

                    "Ticker": ticker,

                    "Current": result["current_price"],

                    "Target": result["target_price"],

                    "Return %": result["expected_return"],

                    "Signal": result["signal"],

                    "Confidence": result["confidence"],

                    "Risk": result["risk_score"],

                    "Position": result["position_size"],

                    "Stop": result["stop_loss"],

                    "R/R": result["risk_reward"],

                    "Volatility": result["volatility"],

                })

            except Exception as e:

                print(f"{ticker}: {e}")

        if not rows:

            return pd.DataFrame()

        result = pd.DataFrame(rows)

        result.sort_values(

            by=[

                "Signal",

                "Return %",

                "Confidence",

            ],

            ascending=[

                True,

                False,

                False,

            ],

            inplace=True,

        )

        result.reset_index(

            drop=True,

            inplace=True,

        )

        return result