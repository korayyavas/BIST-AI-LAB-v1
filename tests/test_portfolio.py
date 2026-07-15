"""
Portfolio Test
BIST AI LAB v3
"""

from config.settings import TICKERS

from services.screener_service import ScreenerService

from portfolio.optimizer import PortfolioOptimizer
from portfolio.allocation import PortfolioAllocation
from portfolio.risk import PortfolioRisk


def main():

    capital = 1_000_000

    screener = ScreenerService()

    optimizer = PortfolioOptimizer()

    allocation = PortfolioAllocation()

    risk = PortfolioRisk()

    print("Portfolio oluşturuluyor...\n")

    df = screener.scan(TICKERS)

    portfolio = optimizer.optimize(

        df,

        max_positions=5,

    )

    portfolio = allocation.allocate(

        portfolio,

        capital,

    )

    metrics = risk.analyze(

        portfolio,

    )

    score = risk.portfolio_score(

        portfolio,

    )

    print(portfolio)

    print("\nPORTFOLIO METRICS\n")

    for k, v in metrics.items():

        print(f"{k:20}: {v}")

    print(f"\nPortfolio Score : {score}")

    print("\nTEST BAŞARILI")


if __name__ == "__main__":

    main()