import sqlalchemy as db


class DatabaseHandler:
    def __init__(self):
        self.engine = db.create_engine('sqlite:///db//notes-sqlalchemy.db')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

        self.notes = db.Table('notes', self.metadata,
                              db.Column("note_id", db.Integer, primary_key=True),
                              db.Column("note_label", db.Text),
                              db.Column("note_content", db.Text))

        self.metadata.create_all(self.engine)

    def __del__(self):
        self.connection.close()

    def insert_new_note(self, label: str, content: str):
        insertion_query = self.notes.insert().values([
            {"note_label": label, "note_content": content}])

        self.connection.execute(insertion_query)
        self.connection.commit()

    def remove_note(self, label: str):
        delete_query = db.delete(self.notes).where(self.notes.c.note_label == label)
        self.connection.execute(delete_query)
        self.connection.commit()

    def get_all_notes(self):
        select_all_query = db.select(self.notes)
        select_all_result = self.connection.execute(select_all_query)
        return select_all_result.fetchall()
