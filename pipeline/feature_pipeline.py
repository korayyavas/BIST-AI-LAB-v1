
"""
Feature Pipeline
BIST AI LAB v3.1
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from indicators.technical_indicators import TechnicalIndicators


class FeaturePipeline:

    def __init__(self, prediction_days: int = 5):

        self.prediction_days = prediction_days
        self.indicators = TechnicalIndicators()

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        df = self.indicators.transform(df)

        self._returns(df)
        self._lags(df)
        self._trend(df)
        self._volatility(df)
        self._volume(df)
        self._price(df)
        self._rolling(df)
        self._levels(df)
        self._target(df)

        return self._clean(df)

    def split_xy(self, df: pd.DataFrame):

        X = df.drop(columns=["TARGET"], errors="ignore")
        X = X.select_dtypes(include=["number"])
        y = df["TARGET"]

        return X, y

    def latest_features(self, df: pd.DataFrame):

        X, _ = self.split_xy(df)
        return X.tail(1)

    def _returns(self, df):

        for w in [1,3,5,10,20]:
            df[f"RETURN_{w}"] = df["Close"].pct_change(w)

    def _lags(self, df):

        for lag in [1,2,3,5,10]:
            df[f"RETURN_LAG_{lag}"] = df["RETURN_1"].shift(lag)
            df[f"VOLUME_LAG_{lag}"] = df["Volume"].pct_change().shift(lag)

    def _trend(self, df):

        for w in [10,20,50]:
            df[f"SMA_{w}"] = df["Close"].rolling(w).mean()
            df[f"EMA_{w}"] = df["Close"].ewm(span=w, adjust=False).mean()

        df["EMA_RATIO"] = df["EMA_20"] / df["EMA_50"]
        df["PRICE_EMA20"] = (df["Close"]-df["EMA_20"]) / df["EMA_20"]
        df["PRICE_EMA50"] = (df["Close"]-df["EMA_50"]) / df["EMA_50"]

    def _volatility(self, df):

        for w in [5,10,20]:
            df[f"VOL_{w}"] = df["RETURN_1"].rolling(w).std()

        if "ATR" in df.columns:
            df["ATR_PERCENT"] = df["ATR"] / df["Close"]

    def _volume(self, df):

        df["VOL_MA20"] = df["Volume"].rolling(20).mean()
        df["VOL_RATIO"] = df["Volume"] / df["VOL_MA20"]
        df["VOL_CHANGE"] = df["Volume"].pct_change()

    def _price(self, df):

        df["BODY"] = df["Close"] - df["Open"]
        df["RANGE"] = df["High"] - df["Low"]
        df["BODY_RATIO"] = df["BODY"] / df["RANGE"]

    def _rolling(self, df):

        for w in [5,10,20]:
            df[f"ROLL_MEAN_{w}"] = df["Close"].rolling(w).mean()
            df[f"ROLL_STD_{w}"] = df["Close"].rolling(w).std()

    def _levels(self, df):

        df["HIGH_252"] = df["High"].rolling(252).max()
        df["LOW_252"] = df["Low"].rolling(252).min()

        df["DIST_HIGH"] = (df["HIGH_252"]-df["Close"]) / df["HIGH_252"]
        df["DIST_LOW"] = (df["Close"]-df["LOW_252"]) / df["LOW_252"]

    def _target(self, df):

        future = df["Close"].shift(-self.prediction_days)
        df["TARGET"] = future / df["Close"] - 1

    def _clean(self, df):

        df = df.replace([np.inf,-np.inf], np.nan)
        df = df.dropna()
        return df.reset_index(drop=True)
