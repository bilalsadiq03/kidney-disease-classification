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
def create_directories(path_to_directories: list, verbose=True) -> None:
    """Creates directories if they don't exist

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: Any) -> None:
    """Saves data to a json file

    Args:
        path (Path): Path to the json file
        data (Any): Data to be saved
    """
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"Data successfully saved to {path}")
    except Exception as e:
        logger.error(f"Error saving data to json file: {e}")
        raise e
    

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
def encode_image_to_base64(image_path: Path) -> str:
    """Encodes an image to a base64 string

    Args:
        image_path (Path): Path to the image file

    Returns:
        str: Base64 encoded string of the image
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        logger.info(f"Image at {image_path} successfully encoded to base64")
        return encoded_string
    except Exception as e:
        logger.error(f"Error encoding image to base64: {e}")
        raise e

@ensure_annotations
def decode_base64_to_image(base64_string: str, output_path: Path) -> None:
    """Decodes a base64 string and saves it as an image file

    Args:
        base64_string (str): Base64 encoded string of the image
        output_path (Path): Path to save the decoded image file
    """
    try:
        image_data = base64.b64decode(base64_string)
        with open(output_path, "wb") as image_file:
            image_file.write(image_data)
        logger.info(f"Base64 string successfully decoded and saved to {output_path}")
    except Exception as e:
        logger.error(f"Error decoding base64 string to image: {e}")
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

@ensure_annotations
def list_files_in_directory(directory_path: Path) -> list:
    """Lists all files in a directory

    Args:
        directory_path (Path): Path to the directory

    Returns:
        list: List of file paths
    """
    try:
        files = [f for f in directory_path.iterdir() if f.is_file()]
        logger.info(f"Listed {len(files)} files in directory {directory_path}")
        return files
    except Exception as e:
        logger.error(f"Error listing files in directory: {e}")
        raise e
    