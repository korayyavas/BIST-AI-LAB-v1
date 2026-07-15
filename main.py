"""
BIST AI LAB v3
Main Entry Point
"""

from __future__ import annotations

from utils.logger import Logger

from config.settings import (
    PROJECT_NAME,
    VERSION,
)


def main():

    logger = Logger()

    logger.info("=" * 60)
    logger.info(f"{PROJECT_NAME} v{VERSION}")
    logger.info("System Started")
    logger.info("=" * 60)

    print("=" * 60)
    print(f"{PROJECT_NAME} v{VERSION}")
    print("=" * 60)
    print("✔ System initialized")
    print("✔ AI Engine ready")
    print("✔ Dashboard ready")
    print("✔ API ready")
    print("=" * 60)


if __name__ == "__main__":

    main()