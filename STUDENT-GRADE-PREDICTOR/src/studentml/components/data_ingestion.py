import pandas as pd
import os
from studentml.logging.logger import logger
from studentml.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def ingest(self):
        logger.info("Reading dataset...")
        df = pd.read_csv(self.config.source_path)
        os.makedirs(os.path.dirname(
            self.config.local_data_path), exist_ok=True)
        df.to_csv(self.config.local_data_path, index=False)
        logger.info(f"Dataset saved to {self.config.local_data_path}")
        return df
