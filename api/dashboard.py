from __future__ import annotations
"""
api/dashboard.py

BIST AI LAB
FastAPI Intelligence Dashboard Router v2

"""



import logging

from fastapi import APIRouter, HTTPException

from services.dashboard_service import (
    get_dashboard,
    dashboard_health,
)


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Intelligence"],
)


@router.get("/{symbol}/summary")
def summary(
    symbol: str,
):

    try:

        data = get_dashboard(
            symbol.upper()
        )


        return {

            "symbol":
            data.get("symbol"),


            "consensus":
            data.get("consensus"),


            "trend":
            data.get("trend"),


            "generated_at":
            data.get("generated_at"),

        }


    except Exception as e:

        logger.exception(
            "Dashboard summary error"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@router.get("/health")
def health():

    return dashboard_health()

@router.get("/{symbol}")
def dashboard(
    symbol: str,
):

    try:

        return get_dashboard(
            symbol.upper()
        )


    except Exception as e:

        logger.exception(
            "Dashboard error"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ============================================================
# SUMMARY
# ============================================================




# ============================================================
# HEALTH
# ============================================================


