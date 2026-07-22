"""
Intelligence Context
BIST AI LAB v10.0
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class IntelligenceContext:

    # =====================================================
    # BASIC
    # =====================================================

    symbol: str

    # =====================================================
    # RAW DATA
    # =====================================================

    prediction: dict = field(default_factory=dict)

    news: list = field(default_factory=list)

    kap: list = field(default_factory=list)

    research: list = field(default_factory=list)

    consensus: dict = field(default_factory=dict)

    # =====================================================
    # AI SCORES
    # =====================================================

    ai_score: float = 50.0

    ml_score: float = 50.0

    technical_score: float = 50.0

    news_score: float = 50.0

    research_score: float = 50.0

    kap_score: float = 50.0

    risk_score: float = 50.0

    consensus_score: float = 50.0

    # =====================================================
    # DECISION
    # =====================================================

    decision: str = "HOLD"

    confidence: float = 50.0

    # =====================================================
    # EXPLAINABLE AI
    # =====================================================

    strengths: list = field(default_factory=list)

    weaknesses: list = field(default_factory=list)

    explanations: list = field(default_factory=list)

    # =====================================================
    # NEWS AI
    # =====================================================

    market_view: str = "NOTR"

    summary: str = ""

    top_story: str = ""

    # =====================================================
    # PORTFOLIO
    # =====================================================

    target_price: float | None = None

    expected_return: float = 0.0

    stop_loss: float | None = None

    take_profit: float | None = None

    # =====================================================
    # RISK
    # =====================================================

    risk_level: str = "MEDIUM"

    # =====================================================
    # SOURCES
    # =====================================================

    source_count: dict = field(

        default_factory=lambda: {

            "news": 0,

            "kap": 0,

            "research": 0,

        }

    )