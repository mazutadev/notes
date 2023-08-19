from note import Note
from validate import str_validate


class Notebook:

    title = str_validate.StrValidate(max_length=255)
    description = str_validate.StrValidate(max_length=255)

    def __init__(self, title: str, description: str):
        self.uid = 0
        self.title = title
        self.description = description
        self.data_list = {}

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value: int):
        if isinstance(value, int):
            self._uid = value
        else:
            raise ValueError("notebook_id должен быть int")


