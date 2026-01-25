import os
import yaml
from src.ds_resume_light_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents.
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as box_exception:
        raise box_exception
    except Exception as e:
        logger.exception(f"Error reading the YAML file: {path_to_yaml}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list[Path]): List of directory paths to create.
        verbose (bool): Whether to log the creation of directories. Defaults to True.
    Returns:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")    

@ensure_annotations
def save_json(path: Path, data: dict[str, Any]) -> None:
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict[str, Any]): Dictionary to save as JSON.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except Exception as e:
        logger.exception(f"Error saving JSON file at: {path}")
        raise e
    
@ensure_annotations
def load_json(path: Path) -> dict[str, Any]:
    """Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): Path to the JSON file.
    Returns:
        dict[str, Any]: Dictionary containing the JSON file contents.
    try:
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        logger.info(f"JSON file loaded from: {path}")
        return data
    except Exception as e:
        logger.exception(f"Error loading JSON file from: {path}")
        raise e
    
@ensure_annotations
def save_binary_file(path: Path, data: Any) -> None:
    """Saves data to a binary file using joblib.

    Args:
        path (Path): Path to save the binary file.
        data (Any): Data to save.
    """
    try:
        with open(path, 'wb') as binary_file:
            joblib.dump(data, binary_file)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.exception(f"Error saving binary file at: {path}")
        raise e
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.
    Returns:
        Any: Data loaded from the binary file.
    try:
    """
    try:
        with open(path, 'rb') as binary_file:
            data = joblib.load(binary_file)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.exception(f"Error loading binary file from: {path}")
        raise e
    