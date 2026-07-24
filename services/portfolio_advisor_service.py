"""
BIST AI LAB
Portfolio AI Advisor Service v1.0
"""


class PortfolioAdvisorService:


    def advise(self, portfolio):


        positions = portfolio.get(
            "positions",
            []
        )


        if not positions:

            return {

                "target_allocation":[],

                "rebalance_required":False,

                "summary":"Portföy verisi yok"

            }





        recommendations = []

        total_score = 0



        for item in positions:


            total_score += item.get(

                "ai_score",

                50

            )



        average_score = (

            total_score /

            len(positions)

        )






        for item in positions:


            symbol = item["symbol"]

            score = item.get(

                "ai_score",

                50

            )


            current_weight = item.get(

                "weight",

                0

            )





            if score >= 70:


                target = 40


            elif score >= 50:


                target = 30


            else:


                target = 20





            recommendations.append({


                "symbol":

                    symbol,


                "current_weight":

                    current_weight,


                "target_weight":

                    target,


                "difference":

                    round(

                        target-current_weight,

                        2

                    )


            })






        return {


            "average_ai_score":

                round(

                    average_score,

                    2

                ),



            "target_allocation":

                recommendations,



            "rebalance_required":

                any(

                    abs(

                        x["difference"]

                    ) > 10

                    for x in recommendations

                ),



            "summary":

                "AI bazlı yeniden dengeleme önerisi hazır."

        }





portfolio_advisor_service = PortfolioAdvisorService()