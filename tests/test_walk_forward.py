"""
Walk Forward Test
BIST AI LAB v4
"""

from data.yahoo_provider import YahooFinanceProvider

from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator

from models.validator import Validator
from models.classification_trainer import ClassificationTrainer

from backtest.walk_forward_backtester import WalkForwardBacktester


def main():

    print("WALK FORWARD TEST")

    provider = YahooFinanceProvider()
    pipeline = FeaturePipeline()
    target = TargetGenerator()
    validator = Validator()
    trainer = ClassificationTrainer()

    df = provider.download("ASELS.IS")

    df = pipeline.transform(df)
    df = target.transform(df)

    X = df.drop(
        columns=["TARGET", "FUTURE_RETURN"],
        errors="ignore",
    )

    X = X.select_dtypes(include=["number"])

    y = df["TARGET"]

    backtester = WalkForwardBacktester(
        trainer=trainer,
        n_splits=5,
    )

    folds, summary = backtester.run(
        X,
        y,
    )

    print()
    print("=" * 60)
    print("WALK FORWARD RESULTS")
    print("=" * 60)
    print(folds)
    print("=" * 60)

    print()

    for k, v in summary.items():
        print(f"{k:12}: {v}")

    print()
    print("TEST BAŞARILI")


if __name__ == "__main__":
    main()
