"""
Trade Log
BIST AI LAB v5
"""

from __future__ import annotations
from pathlib import Path
import pandas as pd


class TradeLog:

    def __init__(self):
        self.rows=[]

    def add(self,date,signal,price,equity):
        self.rows.append({
            "Date":date,
            "Signal":signal,
            "Price":float(price),
            "Equity":float(equity),
        })

    def dataframe(self):
        return pd.DataFrame(self.rows)

    def save_csv(self,path="reports/trade_log.csv"):
        df=self.dataframe()
        p=Path(path)
        p.parent.mkdir(parents=True,exist_ok=True)
        df.to_csv(p,index=False)
        return str(p)
