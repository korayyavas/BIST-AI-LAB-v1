"""
Dashboard Cache Test
"""

from time import perf_counter

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

t0 = perf_counter()

dashboard.analyze("ASELS")

t1 = perf_counter()

dashboard.analyze("ASELS")

t2 = perf_counter()

print()

print("FIRST :", round(t1 - t0, 3), "sec")

print("SECOND:", round(t2 - t1, 3), "sec")