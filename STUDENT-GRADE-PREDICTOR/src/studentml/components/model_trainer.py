import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from studentml.logging.logger import logger
from studentml.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Loading training data...")
        df = pd.read_csv(self.config.training_data_path)

        X = df.drop(columns=["success"])
        y = df["success"]

        logger.info("Splitting train/test...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        logger.info("Training RandomForest model with class_weight='balanced'...")
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            class_weight="balanced",
            random_state=42
        )
        model.fit(X_train, y_train)

        os.makedirs(os.path.dirname(self.config.model_path), exist_ok=True)
        joblib.dump(model, self.config.model_path)
        logger.info(f"✅ Model saved to {self.config.model_path}")
        return model
