import os
import yaml
from studentml.entity.config_entity import (
    DataIngestionConfig, DataTransformationConfig,
    DataValidationConfig, ModelTrainerConfig, ModelEvaluationConfig
)

class ConfigurationManager:
    def __init__(self,
                 config_path="config/config.yaml",
                 params_path="params.yaml",
                 schema_path="schema.yaml"):
        self.config = self.read_yaml(config_path)
        self.params = self.read_yaml(params_path)
        self.schema = self.read_yaml(schema_path)

        os.makedirs(self.config['artifacts_root'], exist_ok=True)

    def read_yaml(self, path_to_yaml: str) -> dict:
        with open(path_to_yaml, 'r') as f:
            return yaml.safe_load(f)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        return DataIngestionConfig(**config)

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config['data_transformation']
        return DataTransformationConfig(**config)

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config['data_validation']
        return DataValidationConfig(**config)

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config['model_trainer']
        return ModelTrainerConfig(**config)

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config['model_evaluation']
        return ModelEvaluationConfig(**config)