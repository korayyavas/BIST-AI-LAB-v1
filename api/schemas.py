"""
API Schemas
BIST AI LAB v3
"""

from __future__ import annotations

from pydantic import BaseModel


class PredictionResponse(BaseModel):

    ticker: str

    current_price: float

    expected_return: float

    target_price: float

    signal: str

    confidence: int

    risk_score: int

    position_size: float

    stop_loss: float

    risk_reward: float

    volatility: float


class HealthResponse(BaseModel):

    project: str

    version: str

    status: str