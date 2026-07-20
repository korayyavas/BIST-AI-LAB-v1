"""
Technical Score Service
BIST AI LAB v7
"""

from __future__ import annotations


class TechnicalScoreService:

    def calculate(self, row):

        score = 50

        try:

            if row["EMA20"] > row["EMA50"]:
                score += 10
            else:
                score -= 10

        except Exception:
            pass

        try:

            rsi = float(row["RSI"])

            if 45 <= rsi <= 65:
                score += 15

            elif rsi > 70:
                score -= 10

            elif rsi < 30:
                score += 10

        except Exception:
            pass

        try:

            if row["MACD"] > row["MACD_SIGNAL"]:
                score += 15
            else:
                score -= 15

        except Exception:
            pass

        return max(0, min(100, round(score, 2)))