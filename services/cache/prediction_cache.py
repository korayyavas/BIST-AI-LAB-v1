"""
Prediction Cache
BIST AI LAB v6

ML prediction result cache layer
"""

from __future__ import annotations

import time
import threading


class PredictionCache:


    def __init__(
        self,
        ttl: int = 300
    ):

        self.ttl = ttl

        self.cache = {}

        self.lock = threading.Lock()



    def get(
        self,
        symbol: str
    ):

        symbol = symbol.upper()


        with self.lock:

            item = self.cache.get(symbol)


            if not item:

                return None



            created = item["time"]


            if time.time() - created > self.ttl:

                del self.cache[symbol]

                return None



            return item["data"]




    def set(
        self,
        symbol: str,
        data
    ):

        symbol = symbol.upper()


        with self.lock:

            self.cache[symbol] = {

                "time": time.time(),

                "data": data

            }




    def clear(self):

        with self.lock:

            self.cache.clear()



prediction_cache = PredictionCache()



__all__ = [

    "PredictionCache",

    "prediction_cache"

]