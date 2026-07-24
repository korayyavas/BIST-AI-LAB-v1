"""
BIST AI LAB
Portfolio Backtest Intelligence Service v1.0
"""


from datetime import datetime





class PortfolioBacktestService:




    def calculate(self, portfolio):


        positions = portfolio.get(

            "positions",

            []

        )



        if not positions:


            return {

                "status":

                    "NO_DATA"

            }







        total_cost = 0

        current_value = 0




        for item in positions:



            total_cost += item.get(

                "cost",

                0

            )


            current_value += item.get(

                "value",

                0

            )







        return_rate = 0



        if total_cost > 0:


            return_rate = (

                (

                    current_value

                    -

                    total_cost

                )

                /

                total_cost

            ) * 100







        return {


            "initial_value":

                round(

                    total_cost,

                    2

                ),



            "current_value":

                round(

                    current_value,

                    2

                ),



            "profit_loss":

                round(

                    current_value-total_cost,

                    2

                ),



            "return_percent":

                round(

                    return_rate,

                    2

                ),



            "benchmark":

                {

                    "name":

                        "BIST100",

                    "comparison":

                        "AI Portfolio"

                },



            "generated_at":

                datetime.utcnow().isoformat()


        }







portfolio_backtest_service = PortfolioBacktestService()