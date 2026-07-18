
"""
Add this code to api/api_server.py
"""

from pydantic import BaseModel
from data.yahoo_provider import YahooFinanceProvider
from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator
from services.prediction_service import PredictionService

class PredictRequest(BaseModel):
    symbol: str

@app.post("/predict")
def predict(req: PredictRequest):
    provider=YahooFinanceProvider()
    pipeline=FeaturePipeline()
    target=TargetGenerator()

    df=provider.download(req.symbol)
    df=pipeline.transform(df)
    df=target.transform(df)

    features=(
        df.drop(columns=["TARGET","FUTURE_RETURN"],errors="ignore")
          .select_dtypes(include=["number"])
    )

    row=df.iloc[[-1]]
    feat=features.iloc[[-1]]
    atr=float(row["ATR"].iloc[0]) if "ATR" in row.columns else 0.0

    result=PredictionService().predict(
        df=row,
        features=feat,
        atr=atr,
    )

    return {"symbol":req.symbol,**result}
    from api.predict_models import PredictRequest
    from services.prediction_controller import PredictionController

    controller=PredictionController()

    @app.post("/predict")
    def predict(req:PredictRequest):
        return {"predictions":[controller.predict(s) for s in req.symbols]}
