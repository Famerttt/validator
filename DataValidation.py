import numpy as np


class Data_validation:
    def __init__(self, data):
        self.data = data

    def _get_deferent_target(self):
        return len(np.unique(self.data.get_dataframe()[self.data.get_target()])) == (int(self.data.get_errorCode()) + 1)

    def _chek_target(self):
        if self.data.get_target() in list(self.data.get_columns()):
            return True
        else:
            return False

    def _checking_for_missing_values(self):
        return self.data.get_dataframe().isnull().values.any()

    def full_validation(self):
        validation_flag = True
        message = ''
        how_many_tasks_the_dataset_is_suitable_for = 0 # задумка на будущее для каких задач датасет

        if self.data.get_target() is None or self.data.get_errorCode() is None:
            print('Подходит для поиска аномалий')
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

            if self._checking_for_missing_values():
                validation_flag = False
                message += '/n There are missing values'

        return validation_flag, message