from __future__ import annotations
"""
services/consensus_service.py

BIST AI LAB
Consensus Decision Engine v2.0

"""



import logging

from dataclasses import dataclass, asdict

from datetime import datetime

from typing import Dict


logger = logging.getLogger(__name__)



# ============================================================
# MODEL
# ============================================================


@dataclass(slots=True)
class ConsensusResult:

    symbol: str

    score: float

    decision: str

    confidence: str

    components: Dict[str, float]

    explanation: str

    timestamp: str



# ============================================================
# CONSENSUS ENGINE
# ============================================================


class ConsensusService:


    WEIGHTS = {


        "news": 0.25,

        "kap": 0.20,

        "research": 0.20,

        "technical": 0.20,

        "ml": 0.15,

    }



    def calculate_score(

        self,

        components: Dict[str, float],

    ) -> float:


        score = 0


        for key, weight in self.WEIGHTS.items():


            value = components.get(

                key,

                50

            )


            score += value * weight



        return round(

            score,

            2

        )



    def decision(

        self,

        score: float,

    ) -> str:


        if score >= 75:

            return "BUY"


        if score >= 55:

            return "HOLD"


        return "SELL"



    def confidence(

        self,

        score: float,

    ) -> str:


        if score >= 80 or score <= 20:

            return "HIGH"


        if score >= 65 or score <= 35:

            return "MEDIUM"


        return "LOW"



    def explain(

        self,

        components: Dict[str, float],

        decision: str,

    ) -> str:


        parts = []


        for key, value in components.items():


            if value >= 70:

                status = "güçlü"

            elif value <= 40:

                status = "zayıf"

            else:

                status = "nötr"


            parts.append(

                f"{key}: {status}"

            )



        return (

            " | ".join(parts)

            +

            f" | Genel karar: {decision}"

        )



    def analyze(

        self,

        symbol: str,

        components: Dict[str, float],

    ):


        score = self.calculate_score(

            components

        )


        decision = self.decision(

            score

        )


        confidence = self.confidence(

            score

        )


        return ConsensusResult(

            symbol=symbol,

            score=score,

            decision=decision,

            confidence=confidence,

            components=components,

            explanation=self.explain(

                components,

                decision

            ),

            timestamp=datetime.utcnow().isoformat(),

        )



# ============================================================
# SINGLETON
# ============================================================


consensus_service = ConsensusService()



# ============================================================
# PUBLIC API
# ============================================================


def calculate_consensus(

    symbol: str,

    components: Dict[str, float],

):


    result = consensus_service.analyze(

        symbol,

        components

    )


    return asdict(

        result

    )



def consensus_health():


    return {


        "service":

        "Consensus Engine",


        "status":

        "ok",

    }



__all__ = [

    "ConsensusResult",

    "ConsensusService",

    "consensus_service",

    "calculate_consensus",

    "consensus_health",

]