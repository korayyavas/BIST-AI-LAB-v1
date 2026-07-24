"""
BIST AI LAB
Market Data API
v10.1

Real Market Data Endpoint
"""

from fastapi import APIRouter, HTTPException

from services.providers.market_data_provider import (
    market_data_provider
)


router = APIRouter(
    prefix="/market",
    tags=["Market Data"]
)



@router.get("/{symbol}")
def get_market_data(
    symbol: str
):


    df = market_data_provider.get(

        symbol

    )


    if df.empty:

        raise HTTPException(

            status_code=404,

            detail="Market data not found"

        )



    latest = df.iloc[-1]


    previous = df.iloc[-2]



    close = float(

        latest["Close"]

    )


    prev_close = float(

        previous["Close"]

    )


    change = close - prev_close



    change_percent = (

        (change / prev_close) * 100

        if prev_close != 0

        else 0

    )




    candles = []



    for _, row in df.tail(250).iterrows():


        candles.append(

            {

                "date":

                    str(

                        row["Date"]

                    ),


                "open":

                    float(

                        row["Open"]

                    ),


                "high":

                    float(

                        row["High"]

                    ),


                "low":

                    float(

                        row["Low"]

                    ),


                "close":

                    float(

                        row["Close"]

                    ),


                "volume":

                    int(

                        row["Volume"]

                    ),

            }

        )





    return {


        "symbol":

            symbol.upper(),



        "source":

            market_data_provider.source,



        "price":

            round(

                close,

                2

            ),



        "change":

            round(

                change,

                2

            ),



        "change_percent":

            round(

                change_percent,

                2

            ),



        "volume":

            int(

                latest["Volume"]

            ),



        "ohlcv":

            candles,


    }