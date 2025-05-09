from studentml.config.configuration import ConfigurationManager
from studentml.components.data_ingestion import DataIngestion
from studentml.logging.logger import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        STAGE_NAME = "Data Ingestion Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            ingestion = DataIngestion(self.config.get_data_ingestion_config())
            ingestion.ingest()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            logger.exception(e)
            raise e
