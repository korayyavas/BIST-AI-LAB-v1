from pydantic import BaseModel

class PredictRequest(BaseModel):
    symbols:list[str]

class PredictionItem(BaseModel):
    symbol:str
    signal:str
    confidence:float
    current_price:float

class PredictResponse(BaseModel):
    predictions:list[PredictionItem]
