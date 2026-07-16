
"""
Error Handler
BIST AI LAB v5.1
"""

from __future__ import annotations

import functools
import logging
import traceback


logger = logging.getLogger("BIST_AI_LAB")


def safe_execute(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            logger.exception("Unhandled exception")
            return {
                "success": False,
                "error": str(exc),
                "traceback": traceback.format_exc(),
            }

    return wrapper
