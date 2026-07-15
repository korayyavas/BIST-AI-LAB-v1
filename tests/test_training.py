"""
Training Service Test
BIST AI LAB v3
"""

from data.yahoo_provider import YahooFinanceProvider
from services.training_service import TrainingService


def main():

    provider = YahooFinanceProvider()

    print("ASELS verisi indiriliyor...")

    df = provider.download("ASELS.IS")

    print(f"Satır Sayısı : {len(df)}")

    service = TrainingService()

    result = service.train(df)

    print("\nMODEL METRICS")
    print(result["metrics"])

    print("\nFEATURE COUNT")
    print(result["features"])

    print("\nTEST BAŞARILI")


if __name__ == "__main__":
    main()