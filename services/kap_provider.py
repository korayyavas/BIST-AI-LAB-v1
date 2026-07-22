from __future__ import annotations
"""
services/providers/kap_provider.py

BIST AI LAB
KAP Data Provider Layer v1.0

"""



import logging

from datetime import datetime

from typing import List, Dict


logger = logging.getLogger(__name__)


class KAPProvider:


    def __init__(self):

        self.source = "KAP"



    def fetch(

        self,

        symbol: str,

    ) -> List[Dict]:

        """
        Gerçek KAP veri bağlantısı için adaptör.

        Şimdilik standart format döndürür.
        """

        logger.info(

            "Fetching KAP data for %s",

            symbol

        )


        return []



    def normalize(

        self,

        raw_items: List[Dict],

        symbol: str,

    ) -> List[Dict]:


        results = []


        for item in raw_items:


            results.append({

                "symbol":

                symbol,


                "title":

                item.get(

                    "title",

                    ""

                ),


                "summary":

                item.get(

                    "summary",

                    ""

                ),


                "category":

                item.get(

                    "category",

                    "OTHER"

                ),


                "published_at":

                item.get(

                    "published_at",

                    datetime.utcnow().isoformat()

                ),


                "url":

                item.get(

                    "url",

                    ""

                )

            })


        return results



kap_provider = KAPProvider()



__all__ = [

    "KAPProvider",

    "kap_provider",

]