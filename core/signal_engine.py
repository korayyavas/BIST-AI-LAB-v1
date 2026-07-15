"""
Signal Engine
BIST AI LAB v3
"""

from __future__ import annotations

from config.settings import (
    BUY_THRESHOLD,
    SELL_THRESHOLD,
    STRONG_BUY,
    STRONG_SELL,
)


class SignalEngine:

    # ==================================================

    def generate(
        self,
        expected_return: float,
    ) -> dict:

        signal = self._signal(
            expected_return
        )

        score = self._confidence(
            expected_return
        )

        return {

            "signal": signal,

            "score": score,

        }

    # ==================================================

    def _signal(
        self,
        expected_return: float,
    ) -> str:

        if expected_return >= STRONG_BUY:
            return "STRONG BUY"

        if expected_return >= BUY_THRESHOLD:
            return "BUY"

        if expected_return <= STRONG_SELL:
            return "STRONG SELL"

        if expected_return <= SELL_THRESHOLD:
            return "SELL"

        return "HOLD"

    # ==================================================

    def _confidence(
        self,
        expected_return: float,
    ) -> int:

        value = abs(expected_return)

        if value >= abs(STRONG_BUY):
            return 100

        score = int(
            50 + value * 800
        )

        return max(
            50,
            min(
                100,
                score,
            ),
        )