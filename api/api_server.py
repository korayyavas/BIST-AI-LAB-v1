
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

startup = Startup()
startup.boot()

app = FastAPI(
    title="BIST AI LAB API",
    version="6.1.0",
)

controller = PredictionController()


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
