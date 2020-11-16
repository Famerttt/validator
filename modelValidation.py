import pandas as pd

# добавим свойства
class ModelValidation:

    def __init__(self, path, target=None, ErrorCode=None):
        self._dataset_path = path
        self._target = target
        self._errorCode = ErrorCode
        self._dataframe = pd.read_csv(path)

    @property
    def dataset_path(self):
        return self._dataset_path

    @dataset_path.setter
    def dataset_path(self, dataset_path):
         self._dataset_path = dataset_path

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
         self._target = target

    @property
    def errorCode(self):
        return self._errorCode

    @errorCode.setter
    def errorCode(self, errorCode ):
         self._errorCode = errorCode

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
         self._dataframe = dataframe

    def get_columns(self):
        return self._dataframe.columns
