"""
FastAPI App
BIST AI LAB v3
"""

from fastapi import FastAPI

from api.routes import router


app = FastAPI(

    title="BIST AI LAB API",

    version="3.0.0",

)

app.include_router(router)