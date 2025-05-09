from src.studentml.pipeline.stage_05_model_evaluation import (
    ModelEvaluationTrainingPipeline)
from src.studentml.pipeline.stage_04_model_trainer import (
    ModelTrainerTrainingPipeline)
from src.studentml.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline)
from src.studentml.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline)
from src.studentml.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline)
from src.studentml.logging.logger import logger
import sys
sys.path.append("src")


def run_stage(stage_name, pipeline_class):
    print(f"\n===== {stage_name} =====")
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline = pipeline_class()
        pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<")
        print(f"✅ {stage_name} completed.")
    except Exception as e:
        logger.exception(e)
        print(f"❌ {stage_name} failed.")
        raise e


if __name__ == "__main__":
    run_stage("Data Ingestion stage", DataIngestionTrainingPipeline)
    run_stage("Data Validation stage", DataValidationTrainingPipeline)
    run_stage("Data Transformation stage", DataTransformationTrainingPipeline)
    run_stage("Model Trainer stage", ModelTrainerTrainingPipeline)
    run_stage("Model Evaluation stage", ModelEvaluationTrainingPipeline)
