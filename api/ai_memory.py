"""
BIST AI LAB
AI Memory API v1.1
"""


from fastapi import APIRouter


from services.ai_memory_service import (

    ai_memory_service,

)






router = APIRouter(

    prefix="/ai-memory",

    tags=["AI Memory"]

)







# ============================================================
# MEMORY SUMMARY
# ============================================================


@router.get("")

def memory_summary():


    return {


        "memory":

            ai_memory_service.calculate_accuracy(),



        "status":

            "ok"


    }







# ============================================================
# AI PERFORMANCE
# ============================================================


@router.get("/performance")

def memory_performance():


    return {


        "performance":

            ai_memory_service.performance(),



        "status":

            "ok"


    }







# ============================================================
# UPDATE DECISION RESULT
# ============================================================


@router.post("/result/{symbol}")

def update_memory_result(


    symbol: str,


    success: bool,


    result: str,


):


    updated = ai_memory_service.update_result(


        symbol.upper(),


        success,


        result


    )



    return {


        "updated":

            updated is not None,



        "data":

            updated


    }







# ============================================================
# SYMBOL MEMORY
# ============================================================


@router.get("/{symbol}")

def symbol_memory(


    symbol: str


):


    return {


        "symbol":

            symbol.upper(),



        "history":

            ai_memory_service.get_memory(


                symbol.upper()


            )

    }