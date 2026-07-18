from pydantic import BaseModel
from typing import Optional


class TopPicksRequest(BaseModel):
    top: int = 5
    signal: Optional[str] = None
    min_confidence: float = 0