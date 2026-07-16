"""
Classification Test
BIST AI LAB v4
"""

from data.yahoo_provider import YahooFinanceProvider

from pipeline.feature_pipeline import FeaturePipeline

from services.prediction_service import PredictionService


def main():

    provider = YahooFinanceProvider()

    pipeline = FeaturePipeline()

    service = PredictionService()

    print("ASELS verisi indiriliyor...")

    df = provider.download("ASELS.IS")

    df = pipeline.transform(df)

    X = pipeline.latest_features(df)

    result = service.predict(

        current_price=float(
            df.iloc[-1]["Close"]
        ),

        atr=float(
            df.iloc[-1]["ATR"]
        ),

        features=X,

    )

    print("\nCLASSIFICATION RESULT\n")

    for key, value in result.items():

        print(f"{key:20}: {value}")

    print("\nTEST BAŞARILI")


if __name__ == "__main__":

    main()