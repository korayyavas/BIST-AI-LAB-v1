"""
Technical Indicators
BIST AI LAB v3.1
"""

from __future__ import annotations

import pandas as pd
import ta


class TechnicalIndicators:

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # Trend
        for w in (10,20,50,100,200):
            df[f"EMA{w}"] = ta.trend.EMAIndicator(close, window=w).ema_indicator()
            df[f"SMA{w}"] = ta.trend.SMAIndicator(close, window=w).sma_indicator()

        df["EMA_RATIO"] = df["EMA20"] / df["EMA50"]
        df["SMA_RATIO"] = df["SMA20"] / df["SMA50"]
        df["EMA_DISTANCE"] = (close - df["EMA20"]) / df["EMA20"]

        # Momentum
        df["RSI"] = ta.momentum.RSIIndicator(close,14).rsi()
        df["RSI_SLOPE"] = df["RSI"].diff()

        macd = ta.trend.MACD(close)
        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_HIST"] = macd.macd_diff()

        for w in (5,10,20):
            df[f"MOM_{w}"] = close.pct_change(w)

        df["ROC"] = ta.momentum.ROCIndicator(close,10).roc()
        df["CCI"] = ta.trend.CCIIndicator(high,low,close).cci()
        df["WILLIAMS_R"] = ta.momentum.WilliamsRIndicator(high,low,close).williams_r()

        stoch = ta.momentum.StochasticOscillator(high,low,close)
        df["STOCH_K"] = stoch.stoch()
        df["STOCH_D"] = stoch.stoch_signal()

        # Volatility
        atr = ta.volatility.AverageTrueRange(high,low,close)
        df["ATR"] = atr.average_true_range()
        df["ATR_PERCENT"] = df["ATR"] / close

        bb = ta.volatility.BollingerBands(close)
        df["BB_UPPER"] = bb.bollinger_hband()
        df["BB_MIDDLE"] = bb.bollinger_mavg()
        df["BB_LOWER"] = bb.bollinger_lband()
        df["BB_WIDTH"] = bb.bollinger_wband()
        df["BB_POSITION"] = (close-df["BB_LOWER"]) / (df["BB_UPPER"]-df["BB_LOWER"])

        kc = ta.volatility.KeltnerChannel(high,low,close)
        df["KC_UPPER"] = kc.keltner_channel_hband()
        df["KC_LOWER"] = kc.keltner_channel_lband()

        # Trend strength
        adx = ta.trend.ADXIndicator(high,low,close)
        df["ADX"] = adx.adx()
        df["ADX_POS"] = adx.adx_pos()
        df["ADX_NEG"] = adx.adx_neg()

        # Volume
        df["OBV"] = ta.volume.OnBalanceVolumeIndicator(close,volume).on_balance_volume()
        df["MFI"] = ta.volume.MFIIndicator(high,low,close,volume).money_flow_index()
        df["VWAP"] = ta.volume.VolumeWeightedAveragePrice(high,low,close,volume).volume_weighted_average_price()

        df["VOL_MA20"] = volume.rolling(20).mean()
        df["REL_VOLUME"] = volume / df["VOL_MA20"]

        # Scores
        df["TREND_SCORE"] = (
            (df["EMA20"] > df["EMA50"]).astype(int)
            + (df["SMA20"] > df["SMA50"]).astype(int)
            + (df["ADX"] > 25).astype(int)
        )

        df["VOLATILITY_SCORE"] = df["ATR_PERCENT"] * 100
        df["MEAN_REVERSION_SCORE"] = 1 - df["BB_POSITION"]
        df["BREAKOUT_SCORE"] = df["BB_WIDTH"] * df["REL_VOLUME"]

        return df
