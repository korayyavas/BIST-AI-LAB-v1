"""
Research Models
BIST AI LAB v7
"""

from pydantic import BaseModel


class ResearchRequest(BaseModel):

    symbol: str