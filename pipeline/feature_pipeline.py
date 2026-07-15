"""
Feature Pipeline
BIST AI LAB v3
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from indicators.technical_indicators import TechnicalIndicators


class FeaturePipeline:

    def __init__(
        self,
        prediction_days: int = 5,
    ):

        self.prediction_days = prediction_days

        self.indicators = TechnicalIndicators()

    # ==================================================
    # MAIN
    # ==================================================

    def transform(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = df.copy()

        # Technical Indicators
        df = self.indicators.transform(df)

        # Returns
        self._returns(df)

        # Lag Features
        self._lags(df)

        # Trend
        self._trend(df)

        # Volatility
        self._volatility(df)

        # Volume
        self._volume(df)

        # Price Action
        self._price_action(df)

        # Target
        self._target(df)

        # Clean
        df = self._clean(df)

        return df

    # ==================================================

    def split_xy(
        self,
        df: pd.DataFrame,
    ):

        drop_columns = [
            "TARGET",
            "Date",
        ]

        existing = [
            c
            for c in drop_columns
            if c in df.columns
        ]

        X = df.drop(
            columns=existing,
        )

        X = X.select_dtypes(
            include=["number"]
        )

        y = df["TARGET"]

        return X, y

    # ==================================================

    def latest_features(
        self,
        df: pd.DataFrame,
    ):

        X, _ = self.split_xy(df)

        return X.tail(1)

    # ==================================================
    # RETURNS
    # ==================================================

    def _returns(
        self,
        df,
    ):

        for window in [1, 3, 5, 10, 20]:

            df[f"RETURN_{window}"] = (
                df["Close"].pct_change(window)
            )

    # ==================================================
    # LAGS
    # ==================================================

    def _lags(
        self,
        df,
    ):

        for lag in [1, 2, 3, 5, 10, 20]:

            df[f"CLOSE_LAG_{lag}"] = (
                df["Close"].shift(lag)
            )

            df[f"VOLUME_LAG_{lag}"] = (
                df["Volume"].shift(lag)
            )

    # ==================================================
    # TREND
    # ==================================================

    def _trend(
        self,
        df,
    ):

        df["SMA20"] = (
            df["Close"]
            .rolling(20)
            .mean()
        )

        df["SMA50"] = (
            df["Close"]
            .rolling(50)
            .mean()
        )

        df["EMA20"] = (
            df["Close"]
            .ewm(span=20)
            .mean()
        )

        df["EMA50"] = (
            df["Close"]
            .ewm(span=50)
            .mean()
        )

        df["EMA_RATIO"] = (
            df["EMA20"]
            / df["EMA50"]
        )

        df["EMA20_DISTANCE"] = (
            (df["Close"] - df["EMA20"])
            / df["EMA20"]
        )

        df["EMA50_DISTANCE"] = (
            (df["Close"] - df["EMA50"])
            / df["EMA50"]
        )

    # ==================================================
    # VOLATILITY
    # ==================================================

    def _volatility(
        self,
        df,
    ):

        for window in [5, 10, 20]:

            df[f"VOLATILITY_{window}"] = (
                df["RETURN_1"]
                .rolling(window)
                .std()
            )

    # ==================================================
    # VOLUME
    # ==================================================

    def _volume(
        self,
        df,
    ):

        df["VOLUME_CHANGE"] = (
            df["Volume"]
            .pct_change()
        )

        df["VOLUME_MA20"] = (
            df["Volume"]
            .rolling(20)
            .mean()
        )

        df["VOLUME_RATIO"] = (
            df["Volume"]
            / df["VOLUME_MA20"]
        )

    # ==================================================
    # PRICE ACTION
    # ==================================================

    def _price_action(
        self,
        df,
    ):

        df["BODY"] = (
            df["Close"]
            - df["Open"]
        )

        df["RANGE"] = (
            df["High"]
            - df["Low"]
        )

        df["BODY_RATIO"] = (
            df["BODY"]
            / df["RANGE"]
        )

    # ==================================================
    # TARGET
    # ==================================================

    def _target(
        self,
        df,
    ):

        future_close = (
            df["Close"]
            .shift(-self.prediction_days)
        )

        df["TARGET"] = (
            future_close
            / df["Close"]
            - 1
        )

    # ==================================================
    # CLEAN
    # ==================================================

    def _clean(
        self,
        df,
    ):

        df = df.replace(
            [np.inf, -np.inf],
            np.nan,
        )

        df = df.dropna()

        df = df.reset_index(
            drop=True
        )

        return df