from __future__ import annotations

"""
api/kap.py

BIST AI LAB
FastAPI KAP Intelligence Router v2

"""


from dataclasses import asdict
import logging

from fastapi import APIRouter, HTTPException

from services.kap_service import (

    get_kap,

    kap_dashboard,

    kap_health,

)


logger = logging.getLogger(__name__)



router = APIRouter(

    prefix="/kap",

    tags=["KAP Intelligence"],

)



# ============================================================
# KAP LIST
# ============================================================


@router.get("/{symbol}")

def kap(

    symbol: str,

):

    try:


        items = get_kap(

            symbol.upper()

        )


        return {


            "symbol":

            symbol.upper(),


            "count":

            len(items),


            "items":
            [
                asdict(item)
                for item in items
            ],

        }



    except Exception as e:


        logger.exception(

            "KAP endpoint error"

        )


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )



# ============================================================
# KAP DASHBOARD
# ============================================================


@router.get("/{symbol}/dashboard")

def dashboard(

    symbol: str,

):


    try:


        return kap_dashboard(

            symbol.upper()

        )


    except Exception as e:


        logger.exception(

            "KAP dashboard error"

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


    return kap_health()