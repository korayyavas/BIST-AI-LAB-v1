
"""
Paper Trading Test
BIST AI LAB v5
"""

from paper.paper_trading_engine import PaperTradingEngine


def main():

    print("PAPER TRADING TEST")

    engine = PaperTradingEngine(initial_cash=100000)

    engine.on_signal("2026-01-02", "BUY", 100.0)
    engine.on_signal("2026-01-03", "HOLD", 102.0)
    engine.on_signal("2026-01-04", "SELL", 110.0)

    report = engine.report()

    print()
    print(report)

    print()
    print("Final Equity :", report.iloc[-1]["Equity"])
    print()
    print("TEST BAŞARILI")


if __name__ == "__main__":
    main()
