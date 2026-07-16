"""
REST API Server
BIST AI LAB v6
"""

from __future__ import annotations

from fastapi import FastAPI

from core.startup import Startup

startup = Startup()
startup.boot()

app = FastAPI(
    title="BIST AI LAB API",
    version="6.0.0",
)

@app.get("/")
def root():
    return {
        "application": "BIST AI LAB",
        "version": "6.0.0",
        "status": "running",
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
    }

@app.get("/system")
def system():
    from core.system_info import SystemInfo
    return SystemInfo.info()