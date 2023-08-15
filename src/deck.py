from notebook import Notebook


class Deck:
    def __init__(self):
        self.deck_id = None
        self.title = None
        self.desc = None
        self.notebooks_list = {}

    def add_notebook(self, notebook: Notebook):
        if isinstance(notebook, Notebook):
            if len(self.notebooks_list) > 0:
                notebook_id = max(self.notebooks_list.keys()) + 1
                notebook.notebook_id = notebook_id
                self.notebooks_list[notebook_id] = notebook
            else:
                notebook.notebook_id = 0
                self.notebooks_list[0] = notebook
        else:
            raise ValueError("В книгу заметок можно добавлять только Note")

    def del_notebook(self, notebook_id: int):
        if notebook_id in self.notebooks_list:
            del self.notebooks_list[notebook_id]
        else:
            print("Ошибка удаления, неправильный notebook_id")

    def print_notebooks(self):
        for notebook_id, notebook in self.notebooks_list.items():
            print(f"dict_notebook_id {notebook_id} : notebook_id {notebook.notebook_id}\n"
                  f"Title: {notebook.title}\nDesc: {notebook.desc}\n")
