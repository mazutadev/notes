from note import Note


def main() -> None:
    first_note = Note("First note", "Note about more Python")

    print(f"Заметка: {first_note.title}\n{first_note.desc}")


if __name__ == "__main__":
    main()