import os
import sys
import numpy as np
import pandas as pd
import dill
from src.logger import logging

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        logging.info(f"Creating directory: {dir_path}")
        os.makedirs(dir_path, exist_ok=True)

        logging.info(f"Saving object to: {file_path}")
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Object saved successfully.")
    except Exception as e:
        logging.error(f"Error occurred while saving object: {e}")
        raise CustomException(e, sys)

