"""
Benchmark Analysis
BIST AI LAB v3.1
"""

from __future__ import annotations

import pandas as pd


class Benchmark:

    # ==================================================

    @staticmethod
    def compare(
        strategy_returns: pd.Series,
        benchmark_returns: pd.Series,
    ) -> pd.DataFrame:

        strategy = strategy_returns.reset_index(
            drop=True
        )

        benchmark = benchmark_returns.reset_index(
            drop=True
        )

        length = min(
            len(strategy),
            len(benchmark),
        )

        strategy = strategy.iloc[:length]

        benchmark = benchmark.iloc[:length]

        return pd.DataFrame(

            {

                "Strategy": strategy,

                "Benchmark": benchmark,

                "Alpha": (
                    strategy - benchmark
                ).round(2),

            }

        )

    # ==================================================

    @staticmethod
    def cumulative(
        returns: pd.Series,
        initial_capital: float = 100000,
    ) -> pd.Series:

        equity = (

            1 + returns / 100

        ).cumprod()

        return (

            equity * initial_capital

        ).round(2)

    # ==================================================

    @staticmethod
    def summary(
        strategy_returns: pd.Series,
        benchmark_returns: pd.Series,
    ) -> dict:

        strategy_total = (

            (1 + strategy_returns / 100)

            .prod()

            - 1

        ) * 100

        benchmark_total = (

            (1 + benchmark_returns / 100)

            .prod()

            - 1

        ) * 100

        alpha = (

            strategy_total

            - benchmark_total

        )

        winner = (

            "Strategy"

            if alpha > 0

            else "Benchmark"

        )

        return {

            "Strategy Return": round(
                strategy_total,
                2,
            ),

            "Benchmark Return": round(
                benchmark_total,
                2,
            ),

            "Alpha": round(
                alpha,
                2,
            ),

            "Winner": winner,

        }

    # ==================================================

    @staticmethod
    def tracking_error(
        strategy_returns: pd.Series,
        benchmark_returns: pd.Series,
    ) -> float:

        diff = (

            strategy_returns.reset_index(
                drop=True
            )

            -

            benchmark_returns.reset_index(
                drop=True
            )

        )

        return round(

            diff.std(),

            4,

        )

    # ==================================================

    @staticmethod
    def information_ratio(
        strategy_returns: pd.Series,
        benchmark_returns: pd.Series,
    ) -> float:

        diff = (

            strategy_returns.reset_index(
                drop=True
            )

            -

            benchmark_returns.reset_index(
                drop=True
            )

        )

        tracking_error = diff.std()

        if tracking_error == 0:

            return 0.0

        return round(

            diff.mean()

            / tracking_error,

            2,

        )