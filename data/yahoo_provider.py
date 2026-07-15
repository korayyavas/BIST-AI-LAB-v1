"""
Yahoo Finance Provider
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd
import yfinance as yf


class YahooFinanceProvider:
    """
    Downloads historical market data from Yahoo Finance.
    """

    def __init__(
        self,
        period: str = "5y",
    ):
        self.period = period

    # --------------------------------------------------

    def download(
        self,
        ticker: str,
    ) -> pd.DataFrame:

        df = yf.download(
            ticker,
            period=self.period,
            progress=False,
            auto_adjust=False,
        )

        if df.empty:
            raise ValueError(f"Veri bulunamadı: {ticker}")

        # MultiIndex sütunları düzleştir
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Date sütununu normal sütun yap
        df = df.reset_index()
        df.columns.name = None

        # Eksik kapanış fiyatlarını sil
        df = df.dropna(subset=["Close"])

        # İndeksi sıfırla
        df = df.reset_index(drop=True)

        return df

    # --------------------------------------------------

    def download_many(
        self,
        tickers: list[str],
    ) -> dict[str, pd.DataFrame]:

        datasets = {}

        for ticker in tickers:

            try:

                datasets[ticker] = self.download(
                    ticker
                )

            except Exception as e:

                print(f"{ticker}: {e}")

        return datasets