
"""
Live Trading Engine Test
BIST AI LAB v5
"""

from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator

from live.live_data_feed import MockLiveDataFeed
from live.live_trading_engine import LiveTradingEngine
from broker.paper_broker import PaperBroker


def main():

    print("LIVE ENGINE TEST")

    provider = YahooFinanceProvider()
    pipeline = FeaturePipeline()
    target = TargetGenerator()

    df = provider.download("ASELS.IS")
    df = pipeline.transform(df)
    df = target.transform(df)

    features = (
        df.drop(columns=["TARGET", "FUTURE_RETURN"], errors="ignore")
          .select_dtypes(include=["number"])
    )

    row = df.iloc[[-1]]
    feat = features.iloc[[-1]]
    atr = float(row["ATR"].iloc[0]) if "ATR" in row.columns else 0.0

    engine = LiveTradingEngine(
        feed=MockLiveDataFeed(),
        broker=PaperBroker(),
    )

    engine.start("ASELS")

    result = engine.process(
        symbol="ASELS",
        df=row,
        features=feat,
        atr=atr,
    )

    engine.stop()

    print()
    print("Tick")
    print(result["tick"])

    print()
    print("Signal")
    print(result["signal"])

    print()
    print("TEST BAŞARILI")


if __name__ == "__main__":
    main()
