
"""
REST API Server
BIST AI LAB v6.1
"""

from __future__ import annotations

from fastapi import FastAPI

from core.startup import Startup
from core.system_info import SystemInfo

from api.predict_models import PredictRequest
from services.prediction_controller import PredictionController

from api.scan_models import ScanRequest
from services.scan_controller import ScanController

from api.top_picks_models import TopPicksRequest
from services.top_picks_controller import TopPicksController
from config.settings import TICKERS

startup = Startup()
startup.boot()

app = FastAPI(
    title="BIST AI LAB API",
    version="6.1.0",
)

controller = PredictionController()
scan_controller = ScanController()
top_picks_controller = TopPicksController()


@app.get("/")
def root():
    return {
        "application": "BIST AI LAB",
        "version": "6.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/system")
def system():
    return SystemInfo.info()


@app.post("/predict")
def predict(req: PredictRequest):
    return {
        "predictions": [
            controller.predict(symbol)
            for symbol in req.symbols
        ]
    }


@app.post("/scan")
def scan(req: ScanRequest):
    return {
        "results": scan_controller.scan(
            symbols=req.symbols,
            signal=req.signal,
            min_confidence=req.min_confidence,
        )
    }


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

