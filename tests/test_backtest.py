"""
Backtest Test
PredictionService uyumlu sürüm
"""

from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator

from services.prediction_service import PredictionService

from backtest.backtest_engine import BacktestEngine
from backtest.performance_metrics import PerformanceMetrics


def main():

    print("BACKTEST TEST")

    provider=YahooFinanceProvider()
    pipeline=FeaturePipeline()
    target=TargetGenerator()
    predictor=PredictionService()

    df=provider.download("ASELS.IS")
    df=pipeline.transform(df)
    df=target.transform(df)

    features=df.select_dtypes(include=["number"]).drop(
        columns=["TARGET","FUTURE_RETURN"],
        errors="ignore",
    )

    signals=[]

    for i in range(len(df)):
        row=df.iloc[[i]]
        feat=features.iloc[[i]]
        atr=float(row["ATR"].iloc[0]) if "ATR" in row.columns else 0.0

        result=predictor.predict(
            row,
            feat,
            atr,
        )
        signals.append(result["signal"])

    df["SIGNAL"]=signals

    engine=BacktestEngine()
    result=engine.run(df)

    metrics=PerformanceMetrics.calculate(result["EQUITY"])

    print("\nBACKTEST RESULTS\n")
    for k,v in metrics.items():
        print(f"{k:20}: {v}")

    print("\nTEST BAŞARILI")


if __name__=="__main__":
    main()
