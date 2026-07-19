"""
BIST AI LAB v3 Configuration
"""

# ==========================================
# PROJECT
# ==========================================

PROJECT_NAME = "BIST AI LAB"

VERSION = "3.0.0"

from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# ==========================================
# DATA
# ==========================================

DEFAULT_PROVIDER = "yfinance"

PERIOD = "5y"

PREDICTION_DAYS = 5

TEST_SIZE = 0.20

TICKERS = [

    "ASELS.IS",

    "THYAO.IS",

    "KCHOL.IS",

    "EREGL.IS",

    "BIMAS.IS",

]

# ==========================================
# MODEL
# ==========================================

MODEL_TYPE = "xgboost"

RANDOM_STATE = 42

N_ESTIMATORS = 300

# ==========================================
# SIGNALS
# ==========================================

BUY_THRESHOLD = 0.03

SELL_THRESHOLD = -0.03

STRONG_BUY = 0.06

STRONG_SELL = -0.06

# ==========================================
# RISK
# ==========================================

INITIAL_CAPITAL = 100_000

MAX_POSITION_SIZE = 0.25

MIN_POSITION_SIZE = 0.05

RISK_PER_TRADE = 0.02

# ==========================================
# PATHS
# ==========================================

DATA_PATH = "data"

MODEL_PATH = "models"

REPORT_PATH = "reports"

LOG_PATH = "logs"

MODEL_FILE = "xgboost_model.joblib"

CLASSIFIER_FILE = "classifier.joblib"

from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")