from note import Note
from notebook import Notebook
from deck import Deck


def main() -> None:

    desck = Deck()

    notebook = Notebook(10, "Тут будут тестовые заметки")
    first_note = Note("Моя первая заметка", "Вы этой заметке я буду писать что-то важное!")

    desck.add_notebook(notebook)
    notebook.add_note(first_note)




if __name__ == "__main__":
    main()
