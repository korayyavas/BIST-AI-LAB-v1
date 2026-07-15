"""
Dashboard Charts
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go


class DashboardCharts:

    # ==================================================

    @staticmethod
    def return_chart(df: pd.DataFrame):

        fig = go.Figure()

        fig.add_bar(

            x=df["Ticker"],

            y=df["Return %"],

            text=df["Return %"].round(2),

            textposition="outside",

            name="Expected Return",

        )

        fig.update_layout(

            title="Expected Return (%)",

            template="plotly_dark",

            height=400,

        )

        return fig

    # ==================================================

    @staticmethod
    def confidence_chart(df: pd.DataFrame):

        fig = go.Figure()

        fig.add_scatter(

            x=df["Ticker"],

            y=df["Confidence"],

            mode="lines+markers",

            name="Confidence",

        )

        fig.update_layout(

            title="Confidence",

            template="plotly_dark",

            height=400,

        )

        return fig

    # ==================================================

    @staticmethod
    def risk_chart(df: pd.DataFrame):

        colors = [

            "green" if x < 35

            else "orange" if x < 70

            else "red"

            for x in df["Risk"]

        ]

        fig = go.Figure()

        fig.add_bar(

            x=df["Ticker"],

            y=df["Risk"],

            marker_color=colors,

            name="Risk",

        )

        fig.update_layout(

            title="Risk Score",

            template="plotly_dark",

            height=400,

        )

        return fig

    # ==================================================

    @staticmethod
    def rr_chart(df: pd.DataFrame):

        fig = go.Figure()

        fig.add_scatter(

            x=df["Ticker"],

            y=df["R/R"],

            mode="markers+text",

            text=df["R/R"].round(2),

            textposition="top center",

            marker=dict(

                size=14,

            ),

            name="Risk / Reward",

        )

        fig.update_layout(

            title="Risk / Reward",

            template="plotly_dark",

            height=400,

        )

        return fig