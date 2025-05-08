import os
import yaml
import json
import joblib
from pathlib import Path
from typing import Any
from studentml.logging.logger import logger

def read_yaml(path_to_yaml: Path) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file loaded: {path_to_yaml}")
        return content

def create_directories(paths: list, verbose=True):
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON saved to: {path}")

def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved to: {path}")

def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data
