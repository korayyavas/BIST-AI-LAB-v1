from __future__ import annotations
"""
Prediction Service
BIST AI LAB v6
Backward-compatible and auto-loads trained model.
"""



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

        buy = float(result.get("buy_probability", 0))
        conf = float(result.get("confidence", 0))
        risk = float(result.get("risk_score", 100))

        top_score = (
            0.50 * buy +
            0.30 * conf +
            0.20 * (100 - risk)
        )

        if top_score >= 60:
            position_size = 0.10
        elif top_score >= 50:
            position_size = 0.08
        elif top_score >= 40:
            position_size = 0.05
        elif top_score >= 30:
            position_size = 0.03
        else:
            position_size = 0.02

        if risk >= 70:
            position_size *= 0.50
        elif risk >= 50:
            position_size *= 0.75

        result["top_score"] = round(top_score, 2)
        result["position_size"] = round(position_size, 2)

        for key, value in list(result.items()):
            try:
                if hasattr(value, "item"):
                    result[key] = value.item()
            except Exception:
                pass

        return result