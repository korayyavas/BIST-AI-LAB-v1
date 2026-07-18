from pydantic import BaseModel


class TopPicksRequest(BaseModel):

    top: int = 10
    signal: str = "BUY"
    min_confidence: float = 70.0