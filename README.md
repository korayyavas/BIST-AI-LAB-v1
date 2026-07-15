# 📈 BIST AI LAB v3

AI-powered algorithmic trading and stock screening platform for Borsa İstanbul.

---

# Features

- XGBoost Machine Learning
- AutoML Hyperparameter Optimization
- Technical Indicator Pipeline
- AI Stock Screener
- Risk Management Engine
- Position Sizing
- Portfolio Optimizer
- Walk Forward Validation
- Backtesting Engine
- Streamlit Dashboard
- FastAPI REST API
- Experiment Tracking
- Model Registry
- Notification System
- Model Storage

---

# Project Structure

```text
BIST_AI_LAB_v3
│
├── api/
├── backtest/
├── config/
├── core/
├── dashboard/
├── data/
├── features/
├── indicators/
├── models/
├── notifications/
├── pipeline/
├── portfolio/
├── reports/
├── research/
├── services/
├── storage/
├── tests/
├── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

```bash
git clone <repository>

cd BIST_AI_LAB_v3

py -m pip install -r requirements.txt
```

---

# Training

```bash
py -m tests.test_training
```

---

# Prediction

```bash
py -m tests.test_prediction
```

---

# AI Screener

```bash
py -m tests.test_screener
```

---

# Portfolio

```bash
py -m tests.test_portfolio
```

---

# Backtest

```bash
py -m tests.test_backtest
```

---

# Dashboard

```bash
py -m streamlit run dashboard/app.py
```

---

# REST API

```bash
py -m uvicorn api.app:app --reload
```

API Docs

```
http://127.0.0.1:8000/docs
```

---

# Technology Stack

- Python 3.13
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit
- Plotly
- FastAPI
- Uvicorn
- yfinance

---

# Current Status

| Module | Status |
|---------|--------|
| Model Engine | ✅ |
| Prediction Engine | ✅ |
| Screener Engine | ✅ |
| Dashboard | ✅ |
| Portfolio Engine | ✅ |
| Backtest Engine | ✅ |
| Research Engine | ✅ |
| Storage Engine | ✅ |
| Notification Engine | ✅ |
| API Engine | ✅ |

---

# Version

```
BIST AI LAB v3.0 RC1
```

---

# License

MIT License

---

Developed with ❤️ using Python.