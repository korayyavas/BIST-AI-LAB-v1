"""
api/__init__.py

BIST AI LAB
FastAPI API Router Package

v6.3
"""


from .dashboard import router as dashboard_router

from .news import router as news_router

from .kap import router as kap_router

from .research import router as research_router

from .decision import router as decision_router

from .top_picks import router as top_picks_router



__all__ = [

    "dashboard_router",

    "news_router",

    "kap_router",

    "research_router",

    "decision_router",

    "top_picks_router",

]