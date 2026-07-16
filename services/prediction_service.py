
"""
Prediction Service
BIST AI LAB v6
Backward-compatible and auto-loads trained model.
"""

from __future__ import annotations

from models.classification_trainer import ClassificationTrainer
from core.signal_engine import SignalEngine


class PredictionService:

    def __init__(self):
        self.trainer = ClassificationTrainer()
        try:
            self.trainer.load()
        except Exception as exc:
            raise RuntimeError(
                "Classifier model could not be loaded. "
                "Run 'py -m tests.test_classifier_training' first."
            ) from exc

        self.engine = SignalEngine()

    def predict(
        self,
        df=None,
        features=None,
        atr=None,
        current_price=None,
        **kwargs,
    ):
        if features is None:
            raise ValueError("features is required")

        probabilities = self.trainer.predict_proba(features)[0]

        if current_price is None:
            if df is None:
                raise ValueError("Either df or current_price must be provided")

            if "Close" in df.columns:
                current_price = float(df["Close"].iloc[0])
            elif "Adj Close" in df.columns:
                current_price = float(df["Adj Close"].iloc[0])
            else:
                raise ValueError("Close price column not found")

        atr = 0.0 if atr is None else float(atr)

        result = self.engine.generate(
            probabilities=probabilities,
            current_price=float(current_price),
            atr=atr,
        )

        for key, value in list(result.items()):
            try:
                if hasattr(value, "item"):
                    result[key] = value.item()
            except Exception:
                pass

        return result
