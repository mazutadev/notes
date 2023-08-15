from note import Note
from notebook import Notebook
from deck import Deck


def main() -> None:

    first_deck = Deck()

    first_notebook = Notebook("Первый блокнот", "Для тестов")

    first_deck.add_notebook(first_notebook)

    first_note = Note("First note", "Note about more Python")
    second_note = Note("Second note", "Note about more Linux")
    third_note = Note("Third note", "Note about more Zabbix")
    forth_note = Note("Fourth note", "Note about more SQL")

    first_notebook.add_note(first_note)
    first_deck.notebooks_list[0].print_notes()


if __name__ == "__main__":
    main()
