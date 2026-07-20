"""
Intelligence Dashboard Test
"""

from services.intelligence_dashboard import IntelligenceDashboard

from services.symbol_analysis_service import SymbolAnalysisService
from services.research_service import ResearchService

from services.news_service import NewsService
from services.kap_service import KapService

from research.consensus.consensus_engine import ConsensusEngine

from core.decision_engine import DecisionEngine


def main():

    dashboard = IntelligenceDashboard(

        symbol_service=SymbolAnalysisService(

            news_service=NewsService(),

            kap_service=KapService(),

            research_service=ResearchService(),

            consensus_engine=ConsensusEngine(),

        ),

        decision_engine=DecisionEngine(),

    )

    result = dashboard.analyze("ASELS")

    print("\nAI INTELLIGENCE\n")

    for k, v in result.items():

        print(f"{k:20}: {v}")

    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()