"""
Equity Curve
BIST AI LAB v5
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


class EquityCurve:

    def __init__(self):
        self.values=[]

    def add(self,date,equity):
        self.values.append({
            "Date":date,
            "Equity":float(equity),
        })

    def dataframe(self):
        df=pd.DataFrame(self.values)
        if not df.empty:
            df["Peak"]=df["Equity"].cummax()
            df["Drawdown"]=((df["Equity"]-df["Peak"])/df["Peak"])*100
        return df

    def save_csv(self,path="reports/equity_curve.csv"):
        df=self.dataframe()
        p=Path(path)
        p.parent.mkdir(parents=True,exist_ok=True)
        df.to_csv(p,index=False)
        return str(p)
