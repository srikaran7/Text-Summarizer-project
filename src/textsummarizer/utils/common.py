import os
from box.exceptions import BoxvalueError
import yaml
from textsummarizer.logging.logger import logger
from ensure import ensure_annotations
from box immport ConfigBox
from pathlib import path
from typing import Any





@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """Read a YAML file and return its contents."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read YAML file from {file_path}")
            return configbox(content)
    except  BoxvalueError:
        raise valueError(f"Yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created at {path}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")


@ensure_annotations
def get_size(path: path) -> str:

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"


