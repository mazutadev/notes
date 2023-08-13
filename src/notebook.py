from note import Note


class Notebook:
    def __init__(self, title: str, desc: str):
        self._title = title
        self._desc = desc
        self._notes_list = {}

    def add_note(self, note: Note):
        if isinstance(note, Note):
            if len(self._notes_list) > 0:
                note_id = max(self._notes_list.keys()) + 1
                note.note_id = note_id
                self._notes_list[note_id] = note
            else:
                note.note_id = 0
                self._notes_list[0] = note
        else:
            raise ValueError("В книгу заметок можно добавлять только Note")

    def del_note(self, note_id: int):
        if note_id in self._notes_list:
            del self._notes_list[note_id]
        else:
            print("Ошибка удаления, неправильный note_id")

    def print_note(self):
        for note_id, note in self._notes_list.items():
            print(f"dict_note_id {note_id} : note_id {note.note_id}\nTitle: {note.title}\nDesc: {note.desc}\n")
