"""
Project Logger
"""

from pathlib import Path
import logging

from config.settings import LOG_PATH


class Logger:

    def __init__(self):

        Path(LOG_PATH).mkdir(exist_ok=True)

        logfile = Path(LOG_PATH) / "bist_ai_lab.log"

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.FileHandler(logfile, encoding="utf-8"),
                logging.StreamHandler(),
            ],
        )

        self.logger = logging.getLogger("BIST_AI_LAB")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)