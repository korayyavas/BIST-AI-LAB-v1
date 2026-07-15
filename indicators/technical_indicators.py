"""
Technical Indicators
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd
import ta


class TechnicalIndicators:

    def transform(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = df.copy()

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # =============================
        # RSI
        # =============================

        df["RSI"] = ta.momentum.RSIIndicator(
            close=close,
            window=14,
        ).rsi()

        # =============================
        # MACD
        # =============================

        macd = ta.trend.MACD(close)

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_HIST"] = macd.macd_diff()

        # =============================
        # EMA
        # =============================

        df["EMA20"] = ta.trend.EMAIndicator(
            close,
            window=20,
        ).ema_indicator()

        df["EMA50"] = ta.trend.EMAIndicator(
            close,
            window=50,
        ).ema_indicator()

        # =============================
        # SMA
        # =============================

        df["SMA20"] = ta.trend.SMAIndicator(
            close,
            window=20,
        ).sma_indicator()

        df["SMA50"] = ta.trend.SMAIndicator(
            close,
            window=50,
        ).sma_indicator()

        # =============================
        # Bollinger
        # =============================

        bb = ta.volatility.BollingerBands(
            close
        )

        df["BB_UPPER"] = bb.bollinger_hband()

        df["BB_MIDDLE"] = bb.bollinger_mavg()

        df["BB_LOWER"] = bb.bollinger_lband()

        df["BB_WIDTH"] = bb.bollinger_wband()

        # =============================
        # ATR
        # =============================

        atr = ta.volatility.AverageTrueRange(
            high,
            low,
            close,
        )

        df["ATR"] = atr.average_true_range()

        # =============================
        # ADX
        # =============================

        adx = ta.trend.ADXIndicator(
            high,
            low,
            close,
        )

        df["ADX"] = adx.adx()

        df["ADX_POS"] = adx.adx_pos()

        df["ADX_NEG"] = adx.adx_neg()

        # =============================
        # CCI
        # =============================

        df["CCI"] = ta.trend.CCIIndicator(
            high,
            low,
            close,
        ).cci()

        # =============================
        # STOCHASTIC
        # =============================

        stoch = ta.momentum.StochasticOscillator(
            high,
            low,
            close,
        )

        df["STOCH_K"] = stoch.stoch()

        df["STOCH_D"] = stoch.stoch_signal()

        # =============================
        # MFI
        # =============================

        df["MFI"] = ta.volume.MFIIndicator(
            high,
            low,
            close,
            volume,
        ).money_flow_index()

        # =============================
        # OBV
        # =============================

        df["OBV"] = ta.volume.OnBalanceVolumeIndicator(
            close,
            volume,
        ).on_balance_volume()

        # =============================
        # ROC
        # =============================

        df["ROC"] = ta.momentum.ROCIndicator(
            close,
            window=10,
        ).roc()

        # =============================
        # WILLIAMS %R
        # =============================

        df["WILLIAMS_R"] = ta.momentum.WilliamsRIndicator(
            high,
            low,
            close,
        ).williams_r()

        return df