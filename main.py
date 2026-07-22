"""
main.py

BIST AI LAB
FastAPI Application Entry Point

"""

from __future__ import annotations

import logging

from fastapi import FastAPI

from api import (

    dashboard_router,

    news_router,

    kap_router,

    research_router,

    decision_router,

)



# ============================================================
# LOGGING
# ============================================================


logging.basicConfig(

    level=logging.INFO,

    format=(

        "%(asctime)s | "

        "%(levelname)s | "

        "%(message)s"

    ),

)


logger = logging.getLogger(__name__)



# ============================================================
# APPLICATION
# ============================================================


app = FastAPI(

    title="BIST AI LAB",

    description=(

        "AI Powered "

        "Borsa Istanbul "

        "Analysis Platform"

    ),

    version="2.0.0",

)



# ============================================================
# ROUTERS
# ============================================================


app.include_router(

    dashboard_router

)


app.include_router(

    news_router

)


app.include_router(

    kap_router

)


app.include_router(

    research_router

)


app.include_router(

    decision_router

)



# ============================================================
# ROOT
# ============================================================


@app.get("/")

def root():

    return {


        "name":

        "BIST AI LAB",


        "version":

        "2.0.0",


        "status":

        "running",


        "modules":

        [

            "News Intelligence",

            "KAP Intelligence",

            "Research Engine",

            "Consensus Engine",

            "Decision Engine",

            "Dashboard",

        ],

    }



# ============================================================
# HEALTH
# ============================================================


@app.get("/health")

def health():

    return {


        "status":

        "ok",


        "service":

        "BIST AI LAB API",

    }