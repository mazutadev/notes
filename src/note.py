from validate import str_validate


class Note:
    title = str_validate.StrValidate(max_length=255)
    description = str_validate.StrValidate(max_length=5000)

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.note_id = 0

    @property
    def note_id(self) -> int:
        return self._note_id

    @note_id.setter
    def note_id(self, value: int):
        if isinstance(value, int):
            self._note_id = value
        else:
            raise ValueError("note_id должен быть int")
