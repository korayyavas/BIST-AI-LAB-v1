from __future__ import annotations
"""
services/decision_service.py

BIST AI LAB
AI Decision Engine v2.0

"""



import logging

from dataclasses import dataclass, asdict

from datetime import datetime

from typing import List, Dict


from services.consensus_service import (
    calculate_consensus,
)


logger = logging.getLogger(__name__)



# ============================================================
# MODEL
# ============================================================


@dataclass(slots=True)
class DecisionResult:

    symbol: str

    decision: str

    score: float

    confidence: str

    risk: str

    reasons: List[str]

    components: Dict[str, float]

    timestamp: str



# ============================================================
# DECISION ENGINE
# ============================================================


class DecisionService:



    def evaluate(

        self,

        symbol: str,

        components: Dict[str, float],

    ):


        consensus = calculate_consensus(

            symbol,

            components

        )


        score = consensus.get(

            "score",

            50

        )


        decision = consensus.get(

            "decision",

            "HOLD"

        )


        confidence = consensus.get(

            "confidence",

            "LOW"

        )


        risk = self.calculate_risk(

            components

        )


        reasons = self.generate_reasons(

            components,

            decision

        )



        return DecisionResult(

            symbol=symbol,

            decision=decision,

            score=score,

            confidence=confidence,

            risk=risk,

            reasons=reasons,

            components=components,

            timestamp=datetime.utcnow().isoformat(),

        )



    # ========================================================
    # RISK
    # ========================================================


    def calculate_risk(

        self,

        components: Dict[str, float],

    ):


        weak = len(

            [

                value

                for value in components.values()

                if value < 40

            ]

        )


        if weak >= 3:

            return "HIGH"


        if weak >= 1:

            return "MEDIUM"


        return "LOW"



    # ========================================================
    # EXPLANATION
    # ========================================================


    def generate_reasons(

        self,

        components: Dict[str, float],

        decision: str,

    ):


        reasons = []


        for key, value in components.items():


            if value >= 70:

                reasons.append(

                    f"{key} positive"

                )


            elif value <= 40:

                reasons.append(

                    f"{key} weak"

                )


            else:

                reasons.append(

                    f"{key} neutral"

                )



        reasons.append(

            f"Final decision: {decision}"

        )


        return reasons



# ============================================================
# SINGLETON
# ============================================================


decision_service = DecisionService()



# ============================================================
# PUBLIC API
# ============================================================


def make_decision(

    symbol: str,

    components: Dict[str, float],

):


    result = decision_service.evaluate(

        symbol,

        components

    )


    return asdict(

        result

    )



def decision_health():


    return {


        "service":

        "AI Decision Engine",


        "status":

        "ok",

    }



__all__ = [

    "DecisionResult",

    "DecisionService",

    "decision_service",

    "make_decision",

    "decision_health",

]