import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import  base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        e: BoxValueError if yaml file is empty

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("YAML file is empty")
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"BoxValueError: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading the yaml file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they don't exist

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")
    

@ensure_annotations
def load_json(path: Path) -> Any:
    """Loads data from a json file

    Args:
        path (Path): Path to the json file
    Returns:
        Any: Data loaded from the json file
    """
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
        logger.info(f"Data successfully loaded from {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from json file: {e}")
        raise e
    
@ensure_annotations
def load_binary_file(file_path: Path) -> Any:
    """Loads data from a binary file using joblib

    Args:
        file_path (Path): Path to the binary file
    Returns:
        Any: Data loaded from the binary file
    """    
    try:
        data = joblib.load(file_path)
        logger.info(f"Data successfully loaded from binary file at {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from binary file: {e}")
        raise e
    
@ensure_annotations
def save_binary_file(file_path: Path, data: Any) -> None:
    """Saves data to a binary file using joblib

    Args:
        file_path (Path): Path to the binary file
        data (Any): Data to be saved
    """
    try:
        joblib.dump(data, file_path)
        logger.info(f"Data successfully saved to binary file at {file_path}")
    except Exception as e:
        logger.error(f"Error saving data to binary file: {e}")
        raise e
    
@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file or directory in KB

    Args:
        path (Path): Path to the file or directory

    Returns:
        str: Size in KB
    """
    size_in_bytes = os.path.getsize(path)
    size_in_kb = size_in_bytes / 1024
    return f"{size_in_kb:.2f} KB"
    


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())



