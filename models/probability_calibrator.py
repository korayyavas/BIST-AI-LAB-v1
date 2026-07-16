"""
Probability Calibrator
BIST AI LAB v4
"""

from __future__ import annotations

from sklearn.calibration import CalibratedClassifierCV


class ProbabilityCalibrator:

    def __init__(self, method: str = "sigmoid", cv: int = 3):
        self.method = method
        self.cv = cv
        self.model = None

    def fit(self, estimator, X_train, y_train):
        self.model = CalibratedClassifierCV(
            estimator=estimator,
            method=self.method,
            cv=self.cv,
        )
        self.model.fit(X_train, y_train)
        return self

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
