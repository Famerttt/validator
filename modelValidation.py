import pandas as pd
import numpy as np


class ModelValidation:

    def __init__(self, path, target=None, ErrorCode=None):
        self._dataset_path = path
        self._target = target
        self._errorCode = ErrorCode
        self._dataframe = pd.read_csv(path)

    def get_dataset_path(self):
        return self._dataset_path

    def get_target(self):
        return self._target

    def get_errorCode(self):
        return self._errorCode

    def get_dataframe(self):
        return self._dataframe

    def get_columns(self):
        return self._dataframe.columns
