import view
import model


class NotesController:
    def __init__(self):
        self.model = model.NotesModel()
        self.view = view.NotesView(controller=self)
        self.view.show_menu()

    def on_show_all_action(self):
        self.view.show_all_notes(self.model.get_all_notes())

    def on_add_new_note_action(self, label: str, content: str):
        self.model.add_new_note(label, content)

    def on_remove_note(self, label: str):
        self.model.remove_note(label)
