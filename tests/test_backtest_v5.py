
"""
Backtest v5 Test
BIST AI LAB v5
"""

from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator

from services.prediction_service import PredictionService

from backtest.backtest_engine import BacktestEngine
from backtest.performance_metrics import PerformanceMetrics


def main():

    print("BACKTEST V5 TEST")

    provider = YahooFinanceProvider()
    pipeline = FeaturePipeline()
    target = TargetGenerator()
    predictor = PredictionService()

    df = provider.download("ASELS.IS")
    df = pipeline.transform(df)
    df = target.transform(df)

    features = (
        df.drop(columns=["TARGET", "FUTURE_RETURN"], errors="ignore")
          .select_dtypes(include=["number"])
    )

    signals = []

    for i in range(len(df)):
        row = df.iloc[[i]]
        feat = features.iloc[[i]]
        atr = float(row["ATR"].iloc[0]) if "ATR" in row.columns else 0.0

        result = predictor.predict(row, feat, atr)
        signals.append(result["signal"])

    df["SIGNAL"] = signals

    engine = BacktestEngine()
    output = engine.run(df)

    metrics = PerformanceMetrics.calculate(
        output["equity"]["Equity"]
    )

    print("\nPERFORMANCE\n")

    for k, v in metrics.items():
        print(f"{k:20}: {v}")

    print("\nTrade Log : reports/trade_log.csv")
    print("Equity    : reports/equity_curve.csv")
    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()
