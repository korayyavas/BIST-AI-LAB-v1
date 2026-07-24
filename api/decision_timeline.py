"""
BIST AI LAB
AI Decision Timeline API v1.0
"""


from fastapi import APIRouter


from services.ai_decision_timeline_service import (

    ai_decision_timeline_service,

)





router = APIRouter(

    prefix="/decision-timeline",

    tags=["AI Decision Timeline"]

)







@router.get("/{symbol}")

def get_decision_history(

    symbol:str

):


    return {


        "symbol":

            symbol.upper(),


        "history":

            ai_decision_timeline_service.get_history(

                symbol.upper()

            )

    }