"""
BIST AI LAB
Portfolio Intelligence Service v1.3
"""

from datetime import datetime


from services.prediction_adapter import prediction_adapter


from services.providers.market_data_provider import (
    market_data_provider,
)


from services.portfolio_risk_service import (
    portfolio_risk_service,
)


from services.portfolio_optimizer_service import (
    portfolio_optimizer_service,
)





class PortfolioService:


    def __init__(self):

        self.positions = [

            {
                "symbol":"ASELS",
                "quantity":100,
                "cost":250
            },

            {
                "symbol":"THYAO",
                "quantity":50,
                "cost":280
            }

        ]





    def normalize_market_data(self, market):


        if hasattr(market.columns, "levels"):


            market.columns = [

                c[0].lower()

                if isinstance(c, tuple)

                else str(c).lower()

                for c in market.columns

            ]


        else:


            market.columns = [

                str(c).lower()

                for c in market.columns

            ]


        return market





    def calculate(self):


        total_value = 0

        total_cost = 0

        result = []





        for item in self.positions:



            symbol = item["symbol"]



            market = market_data_provider.fetch(symbol)



            market = self.normalize_market_data(
                market
            )



            if "close" not in market.columns:


                raise Exception(

                    f"{symbol} close column bulunamadı: {market.columns}"

                )



            price = float(

                market["close"].iloc[-1]

            )



            value = (

                price *

                item["quantity"]

            )



            cost = (

                item["cost"] *

                item["quantity"]

            )



            prediction = prediction_adapter.predict(

                symbol

            )



            ai_score = prediction.get(

                "top_score",

                50

            )



            result.append({


                "symbol":

                    symbol,


                "quantity":

                    item["quantity"],


                "price":

                    round(price,2),


                "value":

                    round(value,2),


                "cost":

                    round(cost,2),


                "ai_score":

                    round(ai_score,2)


            })



            total_value += value

            total_cost += cost






        if total_value > 0:


            for item in result:


                item["weight"] = round(

                    item["value"]

                    /

                    total_value

                    *

                    100,

                    2

                )








        portfolio_score = 0



        if result:


            portfolio_score = round(

                sum(

                    x["ai_score"]

                    for x in result

                )

                /

                len(result),

                2

            )







        portfolio_data = {

            "positions":

                result

        }





        risk = portfolio_risk_service.analyze(

            portfolio_data

        )





        optimization = portfolio_optimizer_service.optimize(

            portfolio_data

        )







        return {


            "portfolio_value":

                round(total_value,2),



            "cost":

                round(total_cost,2),



            "profit_loss":

                round(

                    total_value-total_cost,

                    2

                ),



            "positions":

                result,



            "portfolio_ai_score":

                portfolio_score,



            "risk":

                risk,



            "optimization":

                optimization,



            "timestamp":

                datetime.utcnow().isoformat()


        }





portfolio_service = PortfolioService()




def get_portfolio():


    return portfolio_service.calculate()