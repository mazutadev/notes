from validate import str_validate


class Note:
    title = str_validate.StrValidate(max_length=255)
    description = str_validate.StrValidate(max_length=5000)

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.uid = 0

    @property
    def uid(self) -> int:
        return self._uid

    @uid.setter
    def uid(self, value: int):
        if isinstance(value, int):
            self._uid = value
        else:
            raise ValueError("note_id должен быть int")
