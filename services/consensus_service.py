# -*- coding: utf-8 -*-

"""
BIST AI LAB
Consensus Decision Engine v3.3

Multi Intelligence Decision Layer
"""

from __future__ import annotations

import logging

from dataclasses import dataclass, asdict

from datetime import datetime

from typing import Dict, List


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

    strengths: List[str]

    risks: List[str]

    explanations: List[str]

    explanation: str

    timestamp: str



# ============================================================
# SERVICE
# ============================================================


class ConsensusService:


    WEIGHTS = {

        "ml": 0.35,

        "technical": 0.25,

        "kap": 0.20,

        "news": 0.15,

        "research": 0.05,

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


        distance = abs(
            score - 50
        )


        if distance >= 25:

            return "HIGH"


        if distance >= 12:

            return "MEDIUM"


        return "LOW"



    # ========================================================
    # COMPONENT ANALYSIS
    # ========================================================


    def analyze_components(
        self,
        components: Dict[str, float],
    ):


        strengths = []

        risks = []

        explanations = []



        names = {


            "ml":

            "\u004d\u0061\u006b\u0069\u006e\u0065 \u00f6\u011f\u0072\u0065\u006e\u006d\u0065\u0073\u0069",



            "technical":

            "\u0054\u0065\u006b\u006e\u0069\u006b \u0061\u006e\u0061\u006c\u0069\u007a",



            "news":

            "\u0048\u0061\u0062\u0065\u0072 \u0061\u006e\u0061\u006c\u0069\u007a\u0069",



            "kap":

            "\u004b\u0041\u0050 \u0076\u0065\u0072\u0069\u006c\u0065\u0072\u0069",



            "research":

            "\u0041\u0072\u0061\u015f\u0074\u0131\u0072\u006d\u0061 \u0072\u0061\u0070\u006f\u0072\u006c\u0061\u0072\u0131",

        }




        for key, value in components.items():


            name = names.get(
                key,
                key
            )


            if value >= 70:


                strengths.append(

                    f"{name} g\u00fc\u00e7l\u00fc"

                )


                explanations.append(

                    f"{name} olumlu katk\u0131 sa\u011fl\u0131yor."

                )



            elif value <= 40:


                risks.append(

                    f"{name} zay\u0131f"

                )


                explanations.append(

                    f"{name} a\u015fa\u011f\u0131 y\u00f6nl\u00fc risk olu\u015fturuyor."

                )



            else:


                explanations.append(

                    f"{name} dengeli seviyede."

                )



        return (

            strengths,

            risks,

            explanations

        )



    # ========================================================
    # ANALYZE
    # ========================================================


    def analyze(
        self,
        symbol: str,
        components: Dict[str,float],
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



        strengths, risks, explanations = self.analyze_components(
            components
        )



        explanations.append(

            f"Genel karar: {decision}"

        )



        return ConsensusResult(


            symbol=symbol,


            score=score,


            decision=decision,


            confidence=confidence,


            components=components,


            strengths=strengths,


            risks=risks,


            explanations=explanations,


            explanation=" | ".join(

                explanations

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

    components: Dict[str,float],

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

        "Consensus Decision Engine",


        "version":

        "3.3",


        "status":

        "ok"

    }





__all__ = [

    "ConsensusResult",

    "ConsensusService",

    "consensus_service",

    "calculate_consensus",

    "consensus_health",

]