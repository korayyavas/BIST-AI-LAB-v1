"""
BIST AI LAB
Portfolio Risk Intelligence Service v1.0
"""


class PortfolioRiskService:


    def analyze(self, portfolio):


        positions = portfolio.get(
            "positions",
            []
        )


        if not positions:

            return {

                "risk_level":"UNKNOWN",

                "risk_score":0,

                "warnings":[]

            }





        warnings = []

        risk_score = 0





        for item in positions:


            weight = item.get(
                "weight",
                0
            )


            ai_score = item.get(
                "ai_score",
                50
            )



            if weight > 60:


                warnings.append(

                    f"{item['symbol']} portföy ağırlığı yüksek"

                )


                risk_score += 20





            if ai_score < 40:


                warnings.append(

                    f"{item['symbol']} AI skoru düşük"

                )


                risk_score += 15






        if len(positions) < 3:


            warnings.append(

                "Portföy çeşitlendirmesi düşük"

            )


            risk_score += 20





        risk_score = min(

            risk_score,

            100

        )






        if risk_score >= 70:

            level = "HIGH"


        elif risk_score >= 40:

            level = "MEDIUM"


        else:

            level = "LOW"







        return {


            "risk_level":

                level,


            "risk_score":

                risk_score,


            "warnings":

                warnings,


            "position_count":

                len(positions)


        }





portfolio_risk_service = PortfolioRiskService()