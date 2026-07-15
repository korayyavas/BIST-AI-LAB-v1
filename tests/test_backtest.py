"""
Backtest Test
BIST AI LAB v3
"""

from config.settings import TICKERS

from services.screener_service import ScreenerService

from backtest.strategy import Strategy
from backtest.backtester import Backtester
from backtest.report import BacktestReport


def main():

    screener = ScreenerService()

    strategy = Strategy()

    backtester = Backtester()

    report = BacktestReport()

    print("Backtest çalışıyor...\n")

    df = screener.scan(TICKERS)

    df = strategy.generate(df)

    trades = strategy.trades(df)

    metrics = backtester.run(trades)

    report.print(metrics)

    print()

    print(report.summary(metrics))

    print("\nTEST BAŞARILI")


if __name__ == "__main__":

    main()