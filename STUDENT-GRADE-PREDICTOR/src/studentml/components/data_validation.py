
import pandas as pd
from studentml.logging.logger import logger
from studentml.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate(self):
        logger.info("Validating transformed dataset...")
        df = pd.read_csv(self.config.transformed_data_path)
        missing = df.isnull().sum()
        if missing.any():
            raise ValueError(f"Missing values found: {missing[missing > 0]}")
        logger.info("No missing values found.")
        return True
