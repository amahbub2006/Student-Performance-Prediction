from studentml.config.configuration import ConfigurationManager
from studentml.components.data_validation import DataValidation
from studentml.logging.logger import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        STAGE_NAME = "Data Validation Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            validator = DataValidation(
                self.config.get_data_validation_config())
            validator.validate()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\\n\\n")
        except Exception as e:
            logger.exception(e)
            raise e
