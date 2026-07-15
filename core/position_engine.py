"""
Position Engine
BIST AI LAB v3
"""

from __future__ import annotations


class PositionEngine:

    def __init__(

        self,

        min_position: float = 0.05,

        max_position: float = 0.25,

    ):

        self.min_position = min_position

        self.max_position = max_position

    # ==================================================

    def calculate(

        self,

        confidence: int,

        risk_score: int,

    ) -> float:

        confidence = max(

            0,

            min(100, confidence),

        )

        risk_score = max(

            0,

            min(100, risk_score),

        )

        confidence_weight = confidence / 100

        risk_weight = 1 - (risk_score / 100)

        position = (

            confidence_weight

            * risk_weight

            * self.max_position

        )

        position = max(

            self.min_position,

            position,

        )

        position = min(

            self.max_position,

            position,

        )

        return round(position, 2)

    # ==================================================

    def cash_amount(

        self,

        capital: float,

        position_size: float,

    ) -> float:

        return round(

            capital * position_size,

            2,

        )