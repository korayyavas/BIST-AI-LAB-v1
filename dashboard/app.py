"""
Dashboard v4
BIST AI LAB v4
"""

from __future__ import annotations

import streamlit as st

from config.settings import TICKERS
from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from services.prediction_service_v4 import PredictionServiceV4


st.set_page_config(
    page_title="BIST AI LAB v4",
    layout="wide",
)

st.title("BIST AI LAB v4 - Classification")

provider = YahooFinanceProvider()
pipeline = FeaturePipeline()
service = PredictionServiceV4()

ticker = st.selectbox(
    "Ticker",
    TICKERS,
)

if st.button("Predict"):

    df = provider.download(ticker)
    df = pipeline.transform(df)

    features = pipeline.latest_features(df)

    result = service.predict(
        current_price=float(df.iloc[-1]["Close"]),
        atr=float(df.iloc[-1]["ATR"]),
        features=features,
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Signal", result["signal"])
    c2.metric("Confidence", f'{result["confidence"]:.2f}%')
    c3.metric("Stop Loss", result["stop_loss"])

    st.subheader("Probabilities")

    st.progress(result["buy_probability"] / 100)
    st.write(f'BUY : {result["buy_probability"]:.2f}%')

    st.progress(result["hold_probability"] / 100)
    st.write(f'HOLD : {result["hold_probability"]:.2f}%')

    st.progress(result["sell_probability"] / 100)
    st.write(f'SELL : {result["sell_probability"]:.2f}%')

    st.json(result)
