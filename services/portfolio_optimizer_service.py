"""
BIST AI LAB
Portfolio Optimization Service v1.0
"""


class PortfolioOptimizerService:


    def optimize(self, portfolio):


        positions = portfolio.get(
            "positions",
            []
        )


        if not positions:

            return {

                "recommendation":
                    "NO_DATA",

                "actions":[]

            }




        actions = []



        for item in positions:


            symbol = item.get(
                "symbol"
            )


            weight = item.get(
                "weight",
                0
            )


            ai_score = item.get(
                "ai_score",
                50
            )



            if weight > 60 and ai_score < 40:


                actions.append({

                    "symbol":symbol,

                    "action":
                        "REDUCE",

                    "reason":
                        "Yüksek ağırlık ve düşük AI skoru"

                })



            elif ai_score > 70:


                actions.append({

                    "symbol":symbol,

                    "action":
                        "INCREASE",

                    "reason":
                        "Yüksek AI skoru"

                })


            else:


                actions.append({

                    "symbol":symbol,

                    "action":
                        "HOLD",

                    "reason":
                        "Mevcut ağırlık korunabilir"

                })






        return {


            "optimization":

                actions,


            "summary":

                self.generate_summary(actions)


        }





    def generate_summary(self, actions):


        reduce_count = len([

            x for x in actions

            if x["action"] == "REDUCE"

        ])



        increase_count = len([

            x for x in actions

            if x["action"] == "INCREASE"

        ])




        if reduce_count > 0:

            return "Risk azaltımı öneriliyor."


        if increase_count > 0:

            return "AI skoru yüksek varlıklar artırılabilir."


        return "Portföy dengeli görünüyor."






portfolio_optimizer_service = PortfolioOptimizerService()