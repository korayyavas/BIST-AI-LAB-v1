
"""
Classification Training Service (Optuna)
BIST AI LAB v4
"""

from __future__ import annotations

from pipeline.feature_pipeline import FeaturePipeline
from pipeline.target_generator import TargetGenerator
from pipeline.shap_feature_selector import ShapFeatureSelector

from models.validator import Validator
from models.classification_trainer import ClassificationTrainer
from models.optuna_automl import OptunaAutoML


class ClassificationTrainingService:

    def __init__(self):
        self.pipeline = FeaturePipeline()
        self.target = TargetGenerator()
        self.selector = ShapFeatureSelector(top_n=25)
        self.validator = Validator()
        self.automl = OptunaAutoML(trials=30)
        self.trainer = ClassificationTrainer()

    def train(self, df):

        df = self.pipeline.transform(df)
        df = self.target.transform(df)

        X = df.drop(columns=["TARGET", "FUTURE_RETURN"], errors="ignore")
        X = X.select_dtypes(include=["number"])
        y = df["TARGET"]

        X = self.selector.fit_transform(X, y)

        X_train, X_test, y_train, y_test = self.validator.train_test_split(X, y)

        self.trainer.classifier.model = self.automl.optimize(X_train, y_train)

        pred = self.trainer.classifier.model.predict(X_test)

        metrics = self.trainer.evaluate(y_test, pred)

        self.trainer.save()

        return {
            "metrics": metrics,
            "features": self.selector.feature_count(),
            "selected_features": self.selector.get_features(),
            "best_params": self.automl.best_params,
        }
