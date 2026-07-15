"""
Classification Training Test
BIST AI LAB v4
"""

from data.yahoo_provider import YahooFinanceProvider
from services.classification_training_service import (
    ClassificationTrainingService,
)


def main():

    provider = YahooFinanceProvider()

    print("ASELS verisi indiriliyor...")

    df = provider.download("ASELS.IS")

    service = ClassificationTrainingService()

    result = service.train(df)

    print("\nCLASSIFICATION METRICS\n")

    for k, v in result["metrics"].items():
        print(f"{k:20}: {v}")

    print(f"\nFEATURE COUNT : {result['features']}")

    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()
