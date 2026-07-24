"""
BIST AI LAB
Portfolio Sector Intelligence Service v1.0
"""


class PortfolioSectorService:


    SECTOR_MAP = {


        "ASELS":
            "Savunma Teknoloji",


        "THYAO":
            "Havacılık",


        "GARAN":
            "Bankacılık",


        "AKBNK":
            "Bankacılık",


        "EREGL":
            "Demir Çelik",


        "TUPRS":
            "Enerji",


    }





    def analyze(self, portfolio):


        positions = portfolio.get(
            "positions",
            []
        )


        sectors = {}



        for item in positions:


            symbol = item.get(
                "symbol"
            )


            sector = self.SECTOR_MAP.get(

                symbol,

                "Diğer"

            )


            weight = item.get(

                "weight",

                0

            )



            if sector not in sectors:


                sectors[sector] = 0



            sectors[sector] += weight





        concentration = 0


        if sectors:


            concentration = max(

                sectors.values()

            )





        if concentration >= 70:


            risk = "HIGH"


        elif concentration >= 50:


            risk = "MEDIUM"


        else:


            risk = "LOW"






        return {


            "sectors": sectors,


            "sector_concentration":

                round(

                    concentration,

                    2

                ),


            "sector_risk":

                risk,


            "summary":

                self.generate_summary(

                    risk,

                    concentration

                )

        }





    def generate_summary(

        self,

        risk,

        concentration

    ):


        if risk == "HIGH":

            return (

                f"Sektör yoğunlaşması yüksek. "

                f"En büyük sektör ağırlığı %{concentration}"

            )


        if risk == "MEDIUM":

            return (

                "Sektör dağılımı dengelenebilir."

            )


        return (

            "Sektör dağılımı dengeli."

        )






portfolio_sector_service = PortfolioSectorService()