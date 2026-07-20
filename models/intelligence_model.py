"""
AI Intelligence Model
BIST AI LAB v7
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class IntelligenceModel:

    symbol: str = ""

    decision: str = "HOLD"

    ai_score: float = 0.0

    confidence: float = 0.0

    ml_score: float = 0.0

    technical_score: float = 0.0

    research_score: float = 0.0

    news_score: float = 0.0

    kap_score: float = 0.0

    consensus: str = "HOLD"

    target_price: float = 0.0

    risk: str = "MEDIUM"

    summary: str = ""

    sources: dict = field(default_factory=dict)