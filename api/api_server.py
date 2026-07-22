"""
REST API Server
BIST AI LAB v10.0
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.startup import Startup
from core.system_info import SystemInfo
from config.settings import TICKERS

from api.predict_models import PredictRequest
from api.scan_models import ScanRequest
from api.top_picks_models import TopPicksRequest
from api.intelligence_models import IntelligenceRequest
from api.research_models import ResearchRequest

from services.prediction_controller import PredictionController
from services.scan_controller import ScanController
from services.top_picks_controller import TopPicksController
from services.intelligence_service import IntelligenceService
from services.research_controller import ResearchController

from services.news_service import NewsService
from services.kap_service import KapService

from services.intelligence_dashboard import IntelligenceDashboard
from services.symbol_analysis_service import SymbolAnalysisService

from services.research_service import ResearchService

from research.consensus.consensus_engine import ConsensusEngine

from core.decision_engine import DecisionEngine

# ==========================================================
# STARTUP
# ==========================================================

startup = Startup()
startup.boot()

app = FastAPI(

    title="BIST AI LAB API",

    version="10.0.0",

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

# ==========================================================
# CONTROLLERS
# ==========================================================

prediction_controller = PredictionController()

scan_controller = ScanController()

top_picks_controller = TopPicksController()

research_controller = ResearchController()

intelligence_controller = IntelligenceService()

news_service = NewsService()

kap_service = KapService()

dashboard = IntelligenceDashboard(

    symbol_service=SymbolAnalysisService(

        news_service=news_service,

        kap_service=kap_service,

        research_service=ResearchService(),

        consensus_engine=ConsensusEngine(),

    ),

    decision_engine=DecisionEngine(),

)

# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def root():

    return {

        "application": "BIST AI LAB",

        "version": "10.0.0",

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


# ==========================================================
# PREDICT
# ==========================================================

@app.post("/predict")
def predict(req: PredictRequest):

    return {

        "predictions": [

            prediction_controller.predict(symbol)

            for symbol in req.symbols

        ]

    }


# ==========================================================
# SCAN
# ==========================================================

@app.post("/scan")
def scan(req: ScanRequest):

    return {

        "results": scan_controller.scan(

            symbols=req.symbols,

            signal=req.signal,

            min_confidence=req.min_confidence,

        )

    }


# ==========================================================
# INTELLIGENCE
# ==========================================================

@app.post("/intelligence")
def intelligence(req: IntelligenceRequest):

    return intelligence_controller.analyze(

        req.symbol.upper()

    )


# ==========================================================
# DASHBOARD
# ==========================================================

@app.get("/intelligence/{symbol}")
def intelligence_dashboard(symbol: str):

    return dashboard.analyze(

        symbol.upper()

    )
# ==========================================================
# RESEARCH
# ==========================================================

@app.post("/research")
def research(req: ResearchRequest):

    reports = research_controller.analyze(

        req.symbol.upper()

    )

    return {

        "reports": reports,

    }


# ==========================================================
# NEWS
# ==========================================================

@app.post("/news")
def news(req: IntelligenceRequest):

    news = news_service.get_news(

        req.symbol.upper()

    )

    return {

        "news": [

            item.__dict__

            for item in news

        ]

    }


# ==========================================================
# KAP
# ==========================================================

@app.post("/kap")
def kap(req: IntelligenceRequest):

    announcements = kap_service.get_announcements(

        req.symbol.upper()

    )

    return {

        "kap": [

            item.__dict__

            for item in announcements

        ]

    }


# ==========================================================
# TOP PICKS
# ==========================================================

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


# ==========================================================
# VERSION
# ==========================================================

@app.get("/version")
def version():

    return {

        "application": "BIST AI LAB",

        "version": "10.0.0",

        "ai_engine": "Gemma3 4B (Ollama)",

        "news_ai": "Enabled",

        "intelligence_engine": "v10",

        "status": "Stable",

    }


# ==========================================================
# MODULE STATUS
# ==========================================================

@app.get("/modules")
def modules():

    return {

        "prediction": True,

        "technical": True,

        "news": True,

        "research": True,

        "kap": True,

        "consensus": True,

        "dashboard": True,

        "ollama": True,

        "intelligence": True,

    }


# ==========================================================
# DEBUG
# ==========================================================

@app.get("/debug/{symbol}")
def debug(symbol: str):

    result = intelligence_controller.analyze(

        symbol.upper()

    )

    return {

        "symbol": symbol.upper(),

        "score": result.get("score"),

        "recommendation": result.get("recommendation"),

        "confidence": result.get("confidence"),

        "strengths": result.get("strengths"),

        "weaknesses": result.get("weaknesses"),

        "module_scores": result.get("module_scores"),

        "explanations": result.get("explanations"),

    }


# ==========================================================
# API INFO
# ==========================================================

@app.get("/api")
def api():

    return {

        "name": "BIST AI LAB",

        "version": "10.0.0",

        "endpoints": [

            "/predict",

            "/scan",

            "/top-picks",

            "/research",

            "/news",

            "/kap",

            "/intelligence",

            "/intelligence/{symbol}",

            "/health",

            "/system",

            "/version",

            "/modules",

            "/debug/{symbol}",

        ],

    }