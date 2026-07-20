"""
Portfolio AI Test
"""

from services.portfolio_ai_service import PortfolioAIService

from services.intelligence_dashboard import IntelligenceDashboard
from services.symbol_analysis_service import SymbolAnalysisService
from services.news_service import NewsService
from services.kap_service import KapService
from services.research_service import ResearchService

from research.consensus.consensus_engine import ConsensusEngine

from core.decision_engine import DecisionEngine


dashboard = IntelligenceDashboard(

    symbol_service=SymbolAnalysisService(

        news_service=NewsService(),

        kap_service=KapService(),

        research_service=ResearchService(),

        consensus_engine=ConsensusEngine(),

    ),

    decision_engine=DecisionEngine(),

)

service = PortfolioAIService(dashboard)

portfolio = service.build(

    [

        "ASELS",

        "THYAO",

        "KCHOL",

        "EREGL",

        "BIMAS",

    ]

)

print()

for item in portfolio:

    print(

        item["symbol"],

        item["ai_score"],

        item["decision"],

    )