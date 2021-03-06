import numpy as np


class Data_validation:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return  self.data
    @data.setter
    def data(self, data): # добавить валидацую, проверка на тип класса
        self.data = data
    def _get_deferent_target(self): # проверяем есть ли поломки устроиства, ищем код выхода из строя
        return len(np.unique(self.data.dataframe[self.data.target])) == (int(self.data.errorCode) + 1)

    def _chek_target(self): # проверяем наличие таргета
        if self.data.target in list(self.data.get_columns()):
            return True
        else:
            return False

    def _checking_for_missing_values(self): # есть ли пустые значения
        return self.data.dataframe.isnull().values.any()

    def full_validation(self): # основной цикл валидации, можете подравить. В коде есть недачет
        validation_flag = True
        message = ''
        anomaly = True
        rul = False
        fault = False
        #how_many_tasks_the_dataset_is_suitable_for = 0 # задумка на будущее для каких задач датасет

        if self.data.target is None or self.data.errorCode is None:
            if self._checking_for_missing_values():
                validation_flag = False
                message += 'There are missing values'

        else:

            if not self._chek_target():
                validation_flag = False
                message += "/n model prediction target not set"
            else:
                if not self._get_deferent_target():
                    validation_flag = False
                    message += "Lack of all variations of Bit_code to learn"
                else:
                    rul = True
                    fault = True

            if self._checking_for_missing_values():
                validation_flag = False
                message += '/n There are missing values'

        return validation_flag, message, anomaly, rul, fault