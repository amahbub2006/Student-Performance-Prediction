import pandas as pd
import joblib
import json
import os
from sklearn.metrics import accuracy_score, classification_report
from studentml.logging.logger import logger
from studentml.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        logger.info("Evaluating model...")

        # Ensure report directory exists
        os.makedirs(os.path.dirname(self.config.report_path), exist_ok=True)

        # Load test data and model
        df = pd.read_csv(self.config.test_data_path)
        X = df.drop(columns=["success"])
        y = df["success"]
        model = joblib.load(self.config.model_path)

        # Evaluate
        preds = model.predict(X)
        acc = accuracy_score(y, preds)
        report = classification_report(y, preds, output_dict=True)

        # Save report
        with open(self.config.report_path, "w") as f:
            json.dump({"accuracy": acc, "report": report}, f, indent=4)

        logger.info(f"Evaluation report saved to {self.config.report_path}")
        return acc
