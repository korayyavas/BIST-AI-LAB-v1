"""
REST API Server
BIST AI LAB v7
"""

from __future__ import annotations
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from core.startup import Startup
from core.system_info import SystemInfo
from config.settings import TICKERS

from api.predict_models import PredictRequest
from api.scan_models import ScanRequest
from api.top_picks_models import TopPicksRequest
from api.intelligence_models import IntelligenceRequest
from api.research_models import ResearchRequest
from services.research_controller import ResearchController
from services.prediction_controller import PredictionController
from services.scan_controller import ScanController
from services.top_picks_controller import TopPicksController
from services.intelligence_service import IntelligenceService

from services.intelligence_dashboard import IntelligenceDashboard
from services.symbol_analysis_service import SymbolAnalysisService
from services.news_service import NewsService
from services.kap_service import KapService
from services.research_service import ResearchService

from research.consensus.consensus_engine import ConsensusEngine

from core.decision_engine import DecisionEngine


# ============================================================
# Startup
# ============================================================

startup = Startup()
startup.boot()

app = FastAPI(
    title="BIST AI LAB API",
    version="7.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ============================================================
# Controllers
# ============================================================

controller = PredictionController()

scan_controller = ScanController()

top_picks_controller = TopPicksController()

intelligence_controller = IntelligenceService()

dashboard = IntelligenceDashboard(

    symbol_service=SymbolAnalysisService(

        news_service=NewsService(),

        kap_service=KapService(),

        research_service=ResearchService(),

        consensus_engine=ConsensusEngine(),

    ),

    decision_engine=DecisionEngine(),

)

# ============================================================
# Root
# ============================================================

@app.get("/")
def root():

    return {
        "application": "BIST AI LAB",
        "version": "7.0.0",
        "status": "running",
    }


@app.get("/health")
def health():

    return {
        "status": "ok",
    }


@app.get("/system")
def system():

    return SystemInfo.info()


# ============================================================
# Prediction
# ============================================================

@app.post("/predict")
def predict(req: PredictRequest):

    return {

        "predictions": [

            controller.predict(symbol)

            for symbol in req.symbols

        ]

    }


# ============================================================
# Scan
# ============================================================

@app.post("/scan")
def scan(req: ScanRequest):

    return {

        "results": scan_controller.scan(

            symbols=req.symbols,

            signal=req.signal,

            min_confidence=req.min_confidence,

        )

    }


# ============================================================
# Top Picks
# ============================================================

@app.post("/top-picks")
def top_picks(req: TopPicksRequest):

    return {

        "top_picks": top_picks_controller.get_top(

            symbols=TICKERS,

            top=req.top,

            signal=req.signal,

            min_confidence=req.min_confidence,

        )

    }


# ============================================================
# Intelligence (Legacy)
# ============================================================

@app.post("/intelligence")
def intelligence(req: IntelligenceRequest):

    return intelligence_controller.analyze(req.symbol)


# ============================================================
# Intelligence Dashboard (NEW)
# ============================================================

@app.get("/intelligence/{symbol}")
def intelligence_dashboard(symbol: str):

    return dashboard.analyze(symbol.upper())

research_controller = ResearchController()

@app.post("/research")
def research(req: ResearchRequest):

    reports = research_controller.analyze(req.symbol.upper())

    print("=" * 60)
    print("REPORTS:", reports)
    print("=" * 60)

    return {
        "reports": reports,
    }
# ============================================================
# News
# ============================================================

@app.post("/news")
def news(req: IntelligenceRequest):

    service = NewsService()

    news = service.get_news(req.symbol.upper())

    return {
        "news": [item.__dict__ for item in news]
    }


# ============================================================
# KAP
# ============================================================

@app.post("/kap")
def kap(req: IntelligenceRequest):

    service = KapService()

    events = service.get_announcements(req.symbol.upper())

    return {
        "kap": [item.__dict__ for item in events]
    }

# ============================================================
# KAP
# ============================================================

@app.post("/kap")
def kap(req: IntelligenceRequest):

    service = KapService()

    events = service.get_announcements(req.symbol.upper())

    return {
        "kap": [item.__dict__ for item in events]
    }