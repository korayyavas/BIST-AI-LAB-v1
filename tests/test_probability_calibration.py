
"""
Probability Calibration Test
BIST AI LAB v4
"""

from data.yahoo_provider import YahooFinanceProvider

from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator

from models.validator import Validator
from models.classification_trainer import ClassificationTrainer


def main():

    print("PROBABILITY CALIBRATION TEST")

    provider = YahooFinanceProvider()
    pipeline = FeaturePipeline()
    target = TargetGenerator()

    trainer = ClassificationTrainer()
    validator = Validator()

    df = provider.download("ASELS.IS")

    df = pipeline.transform(df)
    df = target.transform(df)

    X = df.drop(columns=["TARGET", "FUTURE_RETURN"], errors="ignore")
    X = X.select_dtypes(include=["number"])
    y = df["TARGET"]

    X_train, X_test, y_train, y_test = validator.train_test_split(X, y)

    trainer.fit(X_train, y_train)
    trainer.calibrate(X_train, y_train)

    pred = trainer.predict(X_test)
    proba = trainer.predict_proba(X_test)

    metrics = trainer.evaluate(y_test, pred)

    print("\nCALIBRATION METRICS\n")
    for k, v in metrics.items():
        print(f"{k:20}: {v}")

    print("\nFirst Probability:", proba[0])
    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()
