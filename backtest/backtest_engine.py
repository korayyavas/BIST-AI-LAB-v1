
"""
Backtest Engine v5
BIST AI LAB v5
"""

from __future__ import annotations

from backtest.trade_log import TradeLog
from backtest.equity_curve import EquityCurve


class BacktestEngine:

    def __init__(self,
                 initial_cash: float = 100000.0,
                 commission: float = 0.001):

        self.initial_cash = initial_cash
        self.commission = commission

        self.trade_log = TradeLog()
        self.equity_curve = EquityCurve()

    def run(self, df):

        cash = self.initial_cash
        shares = 0.0

        for idx, row in df.iterrows():

            price = float(row["Close"])
            signal = row["SIGNAL"]

            if signal == "BUY" and shares == 0:

                shares = (cash * (1 - self.commission)) / price
                cash = 0.0

                self.trade_log.add(
                    idx,
                    "BUY",
                    price,
                    shares * price,
                )

            elif signal == "SELL" and shares > 0:

                cash = shares * price * (1 - self.commission)
                shares = 0.0

                self.trade_log.add(
                    idx,
                    "SELL",
                    price,
                    cash,
                )

            equity = cash if shares == 0 else shares * price

            self.equity_curve.add(
                idx,
                equity,
            )

        trades = self.trade_log.dataframe()
        equity = self.equity_curve.dataframe()

        self.trade_log.save_csv()
        self.equity_curve.save_csv()

        return {
            "TRADES": trades,
            "EQUITY": equity,

             # Backward compatibility
            "trades": trades,
            "equity": equity,
        }