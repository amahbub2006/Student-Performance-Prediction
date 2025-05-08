import sys
sys.path.append("src")

from src.studentml.logging.logger import logger
from src.studentml.config.configuration import ConfigurationManager

from src.studentml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.studentml.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.studentml.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.studentml.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.studentml.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

# Stage 1: Data Ingestion
STAGE_NAME = "Data Ingestion stage"
try:
    print(f"\n===== {STAGE_NAME} =====")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    print(f"✅ {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    print(f"❌ {STAGE_NAME} failed.")
    raise e

# Stage 2: Data Validation
STAGE_NAME = "Data Validation stage"
try:
    print(f"\n===== {STAGE_NAME} =====")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    print(f"✅ {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    print(f"❌ {STAGE_NAME} failed.")
    raise e

# Stage 3: Data Transformation
STAGE_NAME = "Data Transformation stage"
try:
    print(f"\n===== {STAGE_NAME} =====")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    print(f"✅ {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    print(f"❌ {STAGE_NAME} failed.")
    raise e

# Stage 4: Model Trainer
STAGE_NAME = "Model Trainer stage"
try:
    print(f"\n===== {STAGE_NAME} =====")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = ModelTrainerTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    print(f"✅ {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    print(f"❌ {STAGE_NAME} failed.")
    raise e

# Stage 5: Model Evaluation
STAGE_NAME = "Model Evaluation stage"
try:
    print(f"\n===== {STAGE_NAME} =====")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    pipeline = ModelEvaluationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    print(f"✅ {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    print(f"❌ {STAGE_NAME} failed.")
    raise e