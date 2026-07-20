"""
Intelligence Context
BIST AI LAB v7
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class IntelligenceContext:

    symbol: str

    news: list = field(default_factory=list)

    kap: list = field(default_factory=list)

    research: list = field(default_factory=list)

    consensus: dict = field(default_factory=dict)

    ml_score: float = 0.0

    technical_score: float = 0.0

    research_score: float = 0.0

    news_score: float = 0.0

    kap_score: float = 0.0

    risk_score: float = 0.0