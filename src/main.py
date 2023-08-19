from note import Note
from notebook import Notebook
from deck import Deck
from note_manager import NoteManager


def main() -> None:

    note_manager = NoteManager()
    board = Deck()

    notebook = Notebook("", "Тут будут тестовые заметки")

    first_note = Note("Моя первая заметка", "В этой заметке я буду писать что-то важное!")

    note_manager.add(board, notebook)
    note_manager.add(notebook, first_note)

    print(note_manager.get(notebook, 0).title)


if __name__ == "__main__":
    main()
