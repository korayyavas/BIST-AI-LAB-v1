"""
Prediction Service
BIST AI LAB v3
"""

from __future__ import annotations

from core.predictor import Predictor
from core.signal_engine import SignalEngine
from core.risk_engine import RiskEngine


class PredictionService:

    def __init__(self):

        self.predictor = Predictor()

        self.signal_engine = SignalEngine()

        self.risk_engine = RiskEngine()

    # ==================================================

    def predict(
        self,
        current_price: float,
        features,
        atr: float,
    ) -> dict:

        expected_return = self.predictor.predict_one(
            features
        )

        signal = self.signal_engine.generate(
            expected_return
        )

        risk = self.risk_engine.calculate(

            current_price=current_price,

            expected_return=expected_return,

            atr=atr,

            confidence=signal["score"],

        )

        return {

            "current_price": round(
                current_price,
                2,
            ),

            "expected_return": round(
                expected_return * 100,
                2,
            ),

            "target_price": risk[
                "target_price"
            ],

            "signal": signal[
                "signal"
            ],

            "confidence": signal[
                "score"
            ],

            "risk_score": risk[
                "risk_score"
            ],

            "position_size": risk[
                "position_size"
            ],

            "stop_loss": risk[
                "stop_loss"
            ],

            "risk_reward": risk[
                "risk_reward"
            ],

            "volatility": risk[
                "volatility"
            ],

        }