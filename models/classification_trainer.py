"""
Classification Trainer
BIST AI LAB v5
"""

from __future__ import annotations

from models.classifier import Classifier
from models.classification_metrics import ClassificationMetrics


class ClassificationTrainer:

    def __init__(self):
        self.classifier = Classifier()
        self.selected_features = []

    def fit(self, X_train, y_train):
        self.selected_features = list(X_train.columns)
        self.classifier.fit(X_train, y_train)
        return self

    def predict(self, X):
        X = X[self.selected_features]
        return self.classifier.predict(X)

    def predict_proba(self, X):
        X = X[self.selected_features]
        return self.classifier.predict_proba(X)

    def evaluate(self, y_true, y_pred):
        return ClassificationMetrics.evaluate(y_true, y_pred)

    def save(self):
        self.classifier.save(
            features=self.selected_features,
            version="v5",
        )

    def load(self):
        self.classifier.load()
        self.selected_features = self.classifier.get_features()
        return self
