from __future__ import annotations
"""
api/decision.py

BIST AI LAB
FastAPI AI Decision Router v2

"""



import logging

from fastapi import APIRouter, HTTPException


from services.decision_service import (

    make_decision,

    decision_health,

)



logger = logging.getLogger(__name__)



router = APIRouter(

    prefix="/decision",

    tags=["AI Decision"],

)



# ============================================================
# DECISION
# ============================================================


@router.get("/{symbol}")

def decision(

    symbol: str,

):


    try:


        components = {


            "news":

            50,


            "kap":

            50,


            "research":

            50,


            "technical":

            50,


            "ml":

            50,

        }



        return make_decision(

            symbol.upper(),

            components

        )



    except Exception as e:


        logger.exception(

            "Decision endpoint error"

        )


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )



# ============================================================
# DASHBOARD DECISION
# ============================================================


@router.get("/{symbol}/dashboard")

def dashboard_decision(

    symbol: str,

):


    try:


        return decision(

            symbol

        )



    except Exception as e:


        logger.exception(

            "Decision dashboard error"

        )


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )



# ============================================================
# HEALTH
# ============================================================


@router.get("/health")

def health():


    return decision_health()