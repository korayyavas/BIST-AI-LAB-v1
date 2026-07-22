"""
api/news.py

BIST AI LAB
FastAPI News Router

"""

from __future__ import annotations

import logging

from fastapi import APIRouter, HTTPException, Query

from services.news_service import (

    get_news,

    search_news,

    news_health,

    NewsCategory,

)


logger = logging.getLogger(__name__)



router = APIRouter(

    prefix="/news",

    tags=["News"],

)



# ============================================================
# GET NEWS
# ============================================================


@router.get("/{symbol}")

def news(

    symbol: str,

):


    try:


        result = get_news(

            symbol.upper()

        )


        return {


            "symbol":

            symbol.upper(),


            "count":

            len(result),


            "items":

            result,

        }



    except Exception as e:


        logger.exception(

            "News endpoint error"

        )


        raise HTTPException(

            status_code=500,

            detail=str(e),

        )



# ============================================================
# FILTERED NEWS
# ============================================================


@router.get("/{symbol}/search")

def filtered_news(

    symbol: str,

    score: float = Query(

        0,

        ge=0,

        le=100,

    ),

    sentiment: str | None = None,

):


    try:


        result = search_news(

            symbol.upper(),

            minimum_score=score,

            sentiment=sentiment,

        )


        return {


            "symbol":

            symbol.upper(),


            "count":

            len(result),


            "items":

            result,

        }



    except Exception as e:


        logger.exception(

            "News search error"

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


    return news_health()

