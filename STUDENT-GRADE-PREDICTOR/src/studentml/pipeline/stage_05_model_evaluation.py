from studentml.config.configuration import ConfigurationManager
from studentml.components.model_evaluation import ModelEvaluation
from studentml.logging.logger import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        STAGE_NAME = "Model Evaluation Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            evaluator = ModelEvaluation(
                self.config.get_model_evaluation_config())
            evaluator.evaluate()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\\n\\n")
        except Exception as e:
            logger.exception(e)
            raise e
