from __future__ import annotations
"""
BIST AI LAB
Research Provider v1.0
"""



import logging

from datetime import datetime

from typing import List, Dict


logger = logging.getLogger(__name__)


class ResearchProvider:


    def __init__(self):

        self.source = "Research"



    def fetch(

        self,

        symbol: str,

    ) -> List[Dict]:


        symbol = symbol.upper()


        logger.info(

            "Research provider request: %s",

            symbol

        )


        return self._demo_data(symbol)



    def _demo_data(

        self,

        symbol: str,

    ) -> List[Dict]:


        if symbol != "ASELS":

            return []



        return [

            {

                "institution":

                "Demo Yatırım",


                "recommendation":

                "BUY",


                "target_price":

                250,


                "current_price":

                None,


                "score":

                85,


                "report_date":

                datetime.utcnow().isoformat(),


                "summary":

                "Savunma sanayi büyümesi ve yeni sözleşmeler olumlu değerlendiriliyor."

            }

        ]



    def normalize(

        self,

        raw_items: List[Dict],

        symbol: str,

    ) -> List[Dict]:


        result = []


        for item in raw_items:


            result.append(

                {

                    "symbol":

                    symbol,


                    "institution":

                    item.get(

                        "institution",

                        ""

                    ),


                    "recommendation":

                    item.get(

                        "recommendation",

                        "UNKNOWN"

                    ),


                    "target_price":

                    item.get(

                        "target_price",

                        0

                    ),


                    "score":

                    item.get(

                        "score",

                        0

                    ),


                    "report_date":

                    item.get(

                        "report_date",

                        datetime.utcnow().isoformat()

                    ),


                    "summary":

                    item.get(

                        "summary",

                        ""

                    )

                }

            )


        return result



research_provider = ResearchProvider()


__all__ = [

    "ResearchProvider",

    "research_provider",

]