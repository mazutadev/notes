from note import Note
from notebook import Notebook


def main() -> None:

    first_notebook = Notebook("Первый блокнот", "Для тестов")

    first_note = Note("First note", "Note about more Python")
    second_note = Note("Second note", "Note about more Linux")
    third_note = Note("Third note", "Note about more Zabbix")
    forth_note = Note("Fourth note", "Note about more SQL")


if __name__ == "__main__":
    main()
