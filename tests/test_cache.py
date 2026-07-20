"""
Cache Test
"""

from core.cache_manager import CacheManager


cache = CacheManager()

value = cache.get(

    "ASELS",

    lambda: {

        "score": 88,

        "decision": "BUY",

    },

)

print(value)