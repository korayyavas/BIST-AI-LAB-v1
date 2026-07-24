"""
BIST AI LAB
Main Application v10.4
"""

from __future__ import annotations



# ============================================================
# UTF-8 FIX
# ============================================================

import sys


try:

    sys.stdout.reconfigure(
        encoding="utf-8"
    )

    sys.stderr.reconfigure(
        encoding="utf-8"
    )

except Exception:

    pass





# ============================================================
# IMPORTS
# ============================================================


from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware



from api import (

    dashboard_router,

    news_router,

    kap_router,

    research_router,

    decision_router,

    top_picks_router,

    market_router,

    portfolio_router,

)







# ============================================================
# APPLICATION
# ============================================================


app = FastAPI(

    title="BIST AI LAB",

    description="""

AI destekli Borsa İstanbul analiz platformu.

Modüller:

- Machine Learning Prediction
- Technical Analysis
- News Intelligence
- KAP Analysis
- Research Engine
- Consensus Decision Engine
- Top Picks Engine
- Real Market Data Engine
- Portfolio Intelligence Engine

""",

    version="10.4.0",

)







# ============================================================
# CORS
# ============================================================


app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:3000",

        "http://127.0.0.1:3000",

        "http://localhost:5173",

        "http://127.0.0.1:5173",

        "http://localhost:5174",

        "http://127.0.0.1:5174",

    ],


    allow_credentials=True,


    allow_methods=[

        "*"

    ],


    allow_headers=[

        "*"

    ],

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



app.include_router(

    top_picks_router

)



# REAL MARKET DATA

app.include_router(

    market_router

)





# PORTFOLIO INTELLIGENCE

app.include_router(

    portfolio_router

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

        "10.4.0",


        "status":

        "running"


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

        "BIST AI LAB API"


    }







# ============================================================
# STARTUP
# ============================================================


@app.on_event("startup")

async def startup_event():


    print(

        """

=====================================
 BIST AI LAB v10.4
 API SERVER STARTED

 FEATURES:

 ✓ Dashboard API
 ✓ News Intelligence
 ✓ KAP Analysis
 ✓ Research Engine
 ✓ Decision Engine
 ✓ Top Picks Engine
 ✓ Market Data API
 ✓ Portfolio Intelligence

=====================================

        """

    )