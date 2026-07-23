"""
BIST AI LAB
Top Picks API
v6.3
"""

from fastapi import APIRouter

from services.prediction_adapter import prediction_adapter


router = APIRouter(
    prefix="",
    tags=["Top Picks"]
)


WATCHLIST = [

    "ASELS",
    "THYAO",
    "AKBNK",
    "GARAN",
    "SISE",
    "KCHOL",
    "TUPRS",
    "EREGL",
    "BIMAS",
    "YKBNK",

]


@router.post("/top-picks")
def top_picks(
    payload: dict = None
):

    payload = payload or {}

    top = payload.get(
        "top",
        10
    )


    results = []


    for symbol in WATCHLIST[:top]:

        result = prediction_adapter.predict(
            symbol
        )


        if result.get("status") == "error":

            continue


        results.append(

            {

                "symbol":

                    symbol,


                "signal":

                    result.get(
                        "signal",
                        "HOLD"
                    ),


                "confidence":

                    result.get(
                        "confidence",
                        0
                    ),


                "score":

                    result.get(
                        "top_score",
                        0
                    ),

            }

        )


    results.sort(

        key=lambda x:

        x["score"],

        reverse=True

    )


    return {

        "status":

            "ok",


        "count":

            len(results),


        "top_picks":

            results,

    }



@router.get("/top-picks/health")
def health():

    return {

        "service":

            "Top Picks",


        "status":

            "ok"

    }