"""
Signal Engine v4
BIST AI LAB v4
"""

from __future__ import annotations


class SignalEngineV4:

    def generate(
        self,
        buy_probability: float,
        hold_probability: float,
        sell_probability: float,
    ) -> dict:

        probs = {
            "BUY": buy_probability,
            "HOLD": hold_probability,
            "SELL": sell_probability,
        }

        signal = max(probs, key=probs.get)
        confidence = round(probs[signal] * 100, 2)

        return {
            "signal": signal,
            "confidence": confidence,
            "buy_probability": round(buy_probability * 100, 2),
            "hold_probability": round(hold_probability * 100, 2),
            "sell_probability": round(sell_probability * 100, 2),
        }

    def from_proba(self, probabilities):

        return self.generate(
            probabilities[2],
            probabilities[1],
            probabilities[0],
        )
