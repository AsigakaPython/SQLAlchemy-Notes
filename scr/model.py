import db.database_handler as db


class NotesModel:
    def __init__(self):
        self.db = db.DatabaseHandler()

    def get_all_notes(self):
        return self.db.get_all_notes()

    def add_new_note(self, label: str, content: str):
        self.db.insert_new_note(label, content)

    def remove_note(self, label: str):
        self.db.remove_note(label)
