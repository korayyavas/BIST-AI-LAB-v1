"""
Risk Engine
BIST AI LAB v3
"""

from __future__ import annotations

from core.position_engine import PositionEngine


class RiskEngine:

    def __init__(self):

        self.position_engine = PositionEngine()

    # ==================================================

    def calculate(
        self,
        current_price: float,
        expected_return: float,
        atr: float,
        confidence: int,
    ) -> dict:

        target_price = current_price * (
            1 + expected_return
        )

        stop_loss = current_price - (2 * atr)

        risk = max(
            current_price - stop_loss,
            0.01,
        )

        reward = max(
            target_price - current_price,
            0,
        )

        risk_reward = reward / risk

        volatility = atr / current_price

        risk_score = min(
            100,
            max(
                1,
                int(volatility * 1000),
            ),
        )

        position_size = self.position_engine.calculate(
            confidence=confidence,
            risk_score=risk_score,
        )

        return {

            "target_price": round(target_price, 2),

            "stop_loss": round(stop_loss, 2),

            "risk_reward": round(risk_reward, 2),

            "risk_score": risk_score,

            "position_size": position_size,

            "volatility": round(volatility * 100, 2),

        }