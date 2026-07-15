"""
Training Service
BIST AI LAB v3
"""

from __future__ import annotations

from pipeline.feature_pipeline import FeaturePipeline

from models.trainer import Trainer
from models.automl import AutoML
from models.validator import Validator

from research.experiment_manager import ExperimentManager


class TrainingService:

    def __init__(self):

        self.pipeline = FeaturePipeline()

        self.trainer = Trainer()

        self.automl = AutoML()

        self.validator = Validator()

        self.experiments = ExperimentManager()

    # ==================================================

    def train(
        self,
        df,
    ):

        df = self.pipeline.transform(df)

        X, y = self.pipeline.split_xy(df)

        X_train, X_test, y_train, y_test = (
            self.validator.train_test_split(
                X,
                y,
            )
        )

        self.trainer.model = self.automl.optimize(

            X_train,

            y_train,

        )

        self.trainer.fit(

            X_train,

            y_train,

        )

        prediction = self.trainer.predict(

            X_test,

        )

        metrics = self.trainer.evaluate(

            y_test,

            prediction,

        )

        self.trainer.save()

        self.experiments.save(

            model_name="XGBoost",

            metrics=metrics,

            feature_count=X.shape[1],

        )

        return {

            "metrics": metrics,

            "features": X.shape[1],

        }