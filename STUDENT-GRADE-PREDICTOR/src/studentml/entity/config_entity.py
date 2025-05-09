from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    root_dir: str
    source_path: str
    local_data_path: str


@dataclass
class DataTransformationConfig:
    root_dir: str
    source_path: str
    transformed_data_path: str


@dataclass
class DataValidationConfig:
    root_dir: str
    transformed_data_path: str


@dataclass
class ModelTrainerConfig:
    root_dir: str
    training_data_path: str
    model_path: str


@dataclass
class ModelEvaluationConfig:
    root_dir: str
    test_data_path: str
    model_path: str
    report_path: str
