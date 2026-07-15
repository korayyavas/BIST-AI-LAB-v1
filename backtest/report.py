"""
Backtest Report
BIST AI LAB v3
"""

from __future__ import annotations

import pandas as pd


class BacktestReport:

    # ==================================================

    def summary(
        self,
        metrics: dict,
    ) -> pd.DataFrame:

        return pd.DataFrame(

            [

                {

                    "Metric": "Trades",

                    "Value": metrics["Trades"],

                },

                {

                    "Metric": "Wins",

                    "Value": metrics["Wins"],

                },

                {

                    "Metric": "Losses",

                    "Value": metrics["Losses"],

                },

                {

                    "Metric": "Win Rate",

                    "Value": f"{metrics['Win Rate']} %",

                },

                {

                    "Metric": "Average Return",

                    "Value": f"{metrics['Average Return']} %",

                },

                {

                    "Metric": "Total Return",

                    "Value": f"{metrics['Total Return']} %",

                },

                {

                    "Metric": "Best Trade",

                    "Value": f"{metrics['Best Trade']} %",

                },

                {

                    "Metric": "Worst Trade",

                    "Value": f"{metrics['Worst Trade']} %",

                },

            ]

        )

    # ==================================================

    def print(
        self,
        metrics: dict,
    ):

        print("\n" + "=" * 60)
        print("BACKTEST REPORT")
        print("=" * 60)

        for key, value in metrics.items():

            print(f"{key:20}: {value}")

        print("=" * 60)