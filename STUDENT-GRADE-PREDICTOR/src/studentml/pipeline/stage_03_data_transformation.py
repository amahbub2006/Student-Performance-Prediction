from studentml.config.configuration import ConfigurationManager
from studentml.components.data_transformation import DataTransformation
from studentml.logging.logger import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        STAGE_NAME = "Data Transformation Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            transformer = DataTransformation(self.config.get_data_transformation_config())
            transformer.transform()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\\n\\n")
        except Exception as e:
            logger.exception(e)
            raise e
