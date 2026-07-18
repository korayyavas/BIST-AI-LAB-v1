from services.market_data_service import MarketDataService
from services.prediction_service import PredictionService
from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator

class PredictionController:
    def __init__(self):
        self.market=MarketDataService()
        self.pipeline=FeaturePipeline()
        self.target=TargetGenerator()
        self.service=PredictionService()

    def predict(self,symbol:str):
        df=self.market.download(symbol)
        df=self.pipeline.transform(df)
        df=self.target.transform(df)
        features=df.drop(columns=["TARGET","FUTURE_RETURN"],errors="ignore").select_dtypes(include=["number"])
        row=df.iloc[[-1]]
        feat=features.iloc[[-1]]
        atr=float(row["ATR"].iloc[0]) if "ATR" in row.columns else 0.0
        return {"symbol":symbol,**self.service.predict(df=row,features=feat,atr=atr)}
