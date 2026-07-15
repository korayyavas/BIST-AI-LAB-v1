"""
Prediction Service v4
BIST AI LAB v4
"""

from __future__ import annotations

from core.risk_engine import RiskEngine
from core.signal_engine import SignalEngineV4
from models.classification_trainer import ClassificationTrainer
from pipeline.target_generator import TargetGenerator


class PredictionServiceV4:

    def __init__(self):

        self.trainer = ClassificationTrainer().load()
        self.signal_engine = SignalEngineV4()
        self.risk_engine = RiskEngine()

    # ==================================================

    def predict(
        self,
        current_price: float,
        features,
        atr: float,
    ) -> dict:

        probabilities = self.trainer.predict_proba(features)[0]

        signal = TargetGenerator.probabilities_to_signal(
            probabilities
        )

        risk = self.risk_engine.calculate(
            current_price=current_price,
            expected_return=0.0,
            atr=atr,
            confidence=int(signal["confidence"]),
        )

        return {
            "current_price": round(current_price, 2),
            "signal": signal["signal"],
            "confidence": signal["confidence"],
            "buy_probability": signal["buy_probability"],
            "hold_probability": signal["hold_probability"],
            "sell_probability": signal["sell_probability"],
            "risk_score": risk["risk_score"],
            "position_size": risk["position_size"],
            "stop_loss": risk["stop_loss"],
        }
