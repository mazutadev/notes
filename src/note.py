class Note:
    def __init__(self, title: str, desc: str):
        self._title = title
        self._desc = desc
        self._note_id = None

    # Валидация и получение свойств объекта
    @property
    def title(self) -> str:
        return self._title

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def note_id(self) -> int:
        return self._note_id

    @title.setter
    def title(self, value: str):
        if isinstance(value, str):
            self._title = value
        else:
            raise ValueError("Заголовок должен быть строкой")

    @desc.setter
    def desc(self, value: str):
        if isinstance(value, str):
            self._desc = value
        else:
            raise ValueError("Описание должно быть строкой")

    @note_id.setter
    def note_id(self, value: int):
        if isinstance(value, int):
            self._note_id = value
        else:
            raise ValueError("note_id должен быть int")
