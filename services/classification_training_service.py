"""
Classification Training Service
BIST AI LAB v4
"""

from __future__ import annotations

from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator
from models.validator import Validator
from models.classification_trainer import ClassificationTrainer


class ClassificationTrainingService:

    def __init__(self):

        self.pipeline = FeaturePipeline()
        self.target = TargetGenerator()
        self.validator = Validator()
        self.trainer = ClassificationTrainer()

    def train(self, df):

        df = self.pipeline.transform(df)
        df = self.target.transform(df)

        X = df.drop(columns=["TARGET", "FUTURE_RETURN"], errors="ignore")
        X = X.select_dtypes(include=["number"])
        y = df["TARGET"]

        X_train, X_test, y_train, y_test = (
            self.validator.train_test_split(X, y)
        )

        self.trainer.fit(X_train, y_train)

        pred = self.trainer.predict(X_test)

        metrics = self.trainer.evaluate(
            y_test,
            pred,
        )

        self.trainer.save()

        return {
            "metrics": metrics,
            "features": X.shape[1],
        }
