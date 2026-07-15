"""
AI Trading Dashboard
BIST AI LAB v3
"""

from __future__ import annotations

import streamlit as st

from config.settings import TICKERS
from services.screener_service import ScreenerService
from dashboard.charts import DashboardCharts


st.set_page_config(

    page_title="BIST AI LAB",

    page_icon="📈",

    layout="wide",

)

service = ScreenerService()

charts = DashboardCharts()

# ==================================================

st.sidebar.title("🤖 BIST AI LAB")

tickers = st.sidebar.multiselect(

    "Hisseler",

    TICKERS,

    default=TICKERS,

)

run = st.sidebar.button(

    "🚀 AI Screener",

    use_container_width=True,

)

# ==================================================

st.title("📈 AI Trading Dashboard")

st.caption("BIST AI LAB v3")

# ==================================================

if run:

    with st.spinner("Scanning..."):

        df = service.scan(tickers)

    if df.empty:

        st.warning("Sonuç bulunamadı.")

        st.stop()

    # ==============================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Hisse",
        len(df),
    )

    c2.metric(
        "BUY",
        len(df[df["Signal"].str.contains("BUY")]),
    )

    c3.metric(
        "SELL",
        len(df[df["Signal"].str.contains("SELL")]),
    )

    c4.metric(
        "En İyi Getiri",
        f"{df.iloc[0]['Return %']:.2f} %",
    )

    st.divider()

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True,

    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(

            charts.return_chart(df),

            use_container_width=True,

        )

    with col2:

        st.plotly_chart(

            charts.confidence_chart(df),

            use_container_width=True,

        )

    col3, col4 = st.columns(2)

    with col3:

        st.plotly_chart(

            charts.risk_chart(df),

            use_container_width=True,

        )

    with col4:

        st.plotly_chart(

            charts.rr_chart(df),

            use_container_width=True,

        )

    st.divider()

    st.subheader("🏆 Top 5")

    st.dataframe(

        df.head(5),

        use_container_width=True,

        hide_index=True,

    )

else:

    st.info("Soldan hisseleri seçip AI Screener'i çalıştırın.")