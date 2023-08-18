class StrValidate:
    """Класс валидации строк на минимальное и максимальное значение и на тип данных"""

    @staticmethod
    def __type_validate(value: str) -> str:
        if not isinstance(value, str):
            return str(value)
        else:
            return value

    @staticmethod
    def __length_validate(value: str, min_length: int, max_length: int):
        if len(value) < min_length:
            raise Exception(f"Длина строки меньше минимального значения: {min_length} ")
        elif len(value) > max_length:
            raise Exception(f"Длина строки больше максимального значения: {max_length}")

    def __init__(self, min_length: int = 0, max_length: int = 255):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        getattr(instance, self.name)

    def __set__(self, instance, value):
        str_value = self.__type_validate(value)
        self.__length_validate(str_value, self.min_length, self.max_length)
        setattr(instance, self.name, str_value)
