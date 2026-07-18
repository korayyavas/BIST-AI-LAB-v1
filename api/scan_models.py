from pydantic import BaseModel

class ScanRequest(BaseModel):
    symbols:list[str]
    signal:str|None="BUY"
    min_confidence:float=70.0
