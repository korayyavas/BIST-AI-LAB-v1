"""
Signal Engine
BIST AI LAB v5
"""

from __future__ import annotations


class SignalEngine:

    def generate(
        self,
        probabilities,
        current_price,
        atr,
    ):

        buy=float(probabilities[0])
        hold=float(probabilities[1])
        sell=float(probabilities[2])

        labels=["BUY","HOLD","SELL"]
        idx=max(range(3), key=lambda i: probabilities[i])

        confidence=round(probabilities[idx]*100,2)

        risk=min(100, max(0, int((atr/max(current_price,1e-9))*1000)))

        position_size=round(max(0.02, min(0.10, confidence/1000)),2)

        stop_loss=round(current_price-2*atr,2)

        return {
            "current_price": round(current_price,2),
            "signal": labels[idx],
            "confidence": confidence,
            "buy_probability": round(buy*100,2),
            "hold_probability": round(hold*100,2),
            "sell_probability": round(sell*100,2),
            "risk_score": risk,
            "position_size": position_size,
            "stop_loss": stop_loss,
        }
