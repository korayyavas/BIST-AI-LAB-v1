from __future__ import annotations
"""
api/research.py

BIST AI LAB
FastAPI Research Intelligence Router v2

"""



import logging

from fastapi import APIRouter, HTTPException

from services.research_service import (

    get_research,

    research_dashboard,

    research_health,

    research_service,

)


logger = logging.getLogger(__name__)



router = APIRouter(

    prefix="/research",

    tags=["Research Intelligence"],

)



# ============================================================
# RESEARCH LIST
# ============================================================


@router.get("/{symbol}")

def research(

    symbol: str,

):

    try:


        items = get_research(

            symbol.upper()

        )


        return {


            "symbol":

            symbol.upper(),


            "count":

            len(items),


            "items":

            [

                item

                for item in items

            ],

        }



    except Exception as e:


        logger.exception(

            "Research endpoint error"

        )


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )



# ============================================================
# RESEARCH DASHBOARD
# ============================================================


@router.get("/{symbol}/dashboard")

def dashboard(

    symbol: str,

):

    try:


        return research_dashboard(

            symbol.upper()

        )


    except Exception as e:


        logger.exception(

            "Research dashboard error"

        )


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )



# ============================================================
# RESEARCH CONSENSUS
# ============================================================


@router.get("/{symbol}/consensus")

def consensus(

    symbol: str,

):

    try:


        data = research_dashboard(

            symbol.upper()

        )


        return {


            "symbol":

            symbol.upper(),


            "consensus":

            data.get(

                "consensus",

                {}

            ),

        }



    except Exception as e:


        logger.exception(

            "Research consensus error"

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


    return research_health()