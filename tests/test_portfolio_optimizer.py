
"""
Portfolio Optimizer Test
BIST AI LAB v5
"""

import pandas as pd

from portfolio.portfolio_optimizer import PortfolioOptimizer


def main():

    print("PORTFOLIO OPTIMIZER TEST")

    trades = pd.DataFrame([
        {
            "Entry": 100.0,
            "StopLoss": 95.0,
            "Signal": "BUY",
        },
        {
            "Entry": 120.0,
            "StopLoss": 114.0,
            "Signal": "BUY",
        },
        {
            "Entry": 90.0,
            "StopLoss": 85.0,
            "Signal": "BUY",
        },
    ])

    optimizer = PortfolioOptimizer()

    result = optimizer.optimize(
        trades=trades,
        initial_equity=100000,
    )

    print()
    print(result)

    print()
    print("TEST BAŞARILI")


if __name__ == "__main__":
    main()
