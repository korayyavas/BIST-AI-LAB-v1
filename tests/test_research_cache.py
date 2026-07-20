"""
Research Cache Test
"""

from time import perf_counter

from services.research_service import ResearchService


service = ResearchService()

t0 = perf_counter()

service.get_reports("ASELS")

t1 = perf_counter()

service.get_reports("ASELS")

t2 = perf_counter()

print()

print("FIRST :", round(t1 - t0, 3), "sec")

print("SECOND:", round(t2 - t1, 3), "sec")