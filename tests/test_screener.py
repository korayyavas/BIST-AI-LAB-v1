"""
AI Screener Test
BIST AI LAB v3
"""

from config.settings import TICKERS

from services.screener_service import ScreenerService


def main():

    service = ScreenerService()

    print("AI Screener çalışıyor...\n")

    result = service.scan(TICKERS)

    if result.empty:

        print("Sonuç bulunamadı.")

        return

    print(result)

    print("\nTop 5\n")

    print(result.head())

    print("\nToplam Hisse :", len(result))

    print("\nTEST BAŞARILI")


if __name__ == "__main__":

    main()