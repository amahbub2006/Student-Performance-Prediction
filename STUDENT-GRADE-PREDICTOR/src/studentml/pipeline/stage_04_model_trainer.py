from studentml.config.configuration import ConfigurationManager
from studentml.components.model_trainer import ModelTrainer
from studentml.logging.logger import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        STAGE_NAME = "Model Trainer Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            trainer = ModelTrainer(self.config.get_model_trainer_config())
            trainer.train()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\\n\\n")
        except Exception as e:
            logger.exception(e)
            raise e
