from pydantic import BaseModel


class IntelligenceRequest(BaseModel):
    symbol: str