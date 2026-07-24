"""
BIST AI LAB
Portfolio AI Report Generator v1.0
"""


from datetime import datetime





class PortfolioReportService:




    def generate(self, portfolio):


        value = portfolio.get(
            "portfolio_value",
            0
        )


        profit = portfolio.get(
            "profit_loss",
            0
        )


        score = portfolio.get(
            "portfolio_ai_score",
            0
        )


        risk = portfolio.get(
            "risk",
            {}
        )


        optimization = portfolio.get(
            "optimization",
            {}
        )


        advisor = portfolio.get(
            "advisor",
            {}
        )


        sector = portfolio.get(
            "sector_analysis",
            {}
        )





        report = []



        report.append(

            f"Portföy toplam değeri {value} TL."

        )



        if profit >= 0:


            report.append(

                f"Portföy kâr durumu pozitif: +{profit} TL."

            )


        else:


            report.append(

                f"Portföy zararda: {profit} TL."

            )





        report.append(

            f"AI portföy skoru {score}/100."

        )





        report.append(

            f"Risk seviyesi {risk.get('risk_level','UNKNOWN')} "
            f"({risk.get('risk_score',0)})."

        )





        if risk.get("warnings"):


            report.append(

                "Risk uyarıları: "

                +

                ", ".join(

                    risk["warnings"]

                )

            )





        if optimization.get("summary"):


            report.append(

                optimization["summary"]

            )





        if advisor.get("rebalance_required"):


            report.append(

                "AI Advisor yeniden dengeleme öneriyor."

            )


        else:


            report.append(

                "Portföy dengesi korunabilir."

            )





        if sector.get("summary"):


            report.append(

                sector["summary"]

            )






        return {


            "title":

                "BIST AI LAB Portfolio Intelligence Report",



            "summary":

                " ".join(report),



            "risk":

                risk,



            "recommendation":

                optimization.get(

                    "summary",

                    "HOLD"

                ),



            "generated_at":

                datetime.utcnow().isoformat()


        }







portfolio_report_service = PortfolioReportService()