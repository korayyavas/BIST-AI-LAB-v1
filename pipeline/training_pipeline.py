"""
Training Pipeline
BIST AI LAB v3
"""

from sklearn.model_selection import train_test_split

from config.settings import (
    TEST_SIZE,
    RANDOM_STATE,
)


class TrainingPipeline:

    def split(
        self,
        X,
        y,
    ):

        return train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            shuffle=False,
        )

    # -----------------------------------------

    def fit(
        self,
        model,
        X_train,
        y_train,
    ):

        model.fit(
            X_train,
            y_train,
        )

        return model

    # -----------------------------------------

    def predict(
        self,
        model,
        X_test,
    ):

        return model.predict(
            X_test
        )