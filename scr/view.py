import os

from art import tprint
from prettytable import PrettyTable


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class NotesView:
    def __init__(self, controller):
        self.controller = controller

    def show_menu(self):
        clear()
        tprint("Asigaka   Notes")
        print("=======================")
        print("Main Menu")
        print("")
        print("1. Show All Notes")
        print("2. Add New Note")
        print("3. Remove Note")
        print("4. Exit")
        print("")
        option = int(input("Choose Option: "))
        print("=======================")

        if option == 1:
            self.on_show_all_notes()
        elif option == 2:
            self.on_add_new_note()
        elif option == 3:
            self.on_remove_note()
        elif option == 4:
            exit(0)
        else:
            print("Wrong option!")

    def on_show_all_notes(self):
        self.controller.on_show_all_action()
        input("Press Enter")
        self.show_menu()

    def on_add_new_note(self):
        label = input("Enter Note's label: ")
        content = input("Enter Note's content: ")
        self.controller.on_add_new_note_action(label, content)
        input("Press Enter")
        self.show_menu()

    def on_remove_note(self):
        label = input("Enter Note's label: ")
        self.controller.on_remove_note(label)
        input("Press Enter")
        self.show_menu()

    def show_all_notes(self, notes):
        if len(notes) == 0:
            print("You haven't any notes")
            return

        notes_table = PrettyTable()
        notes_table.field_names = ["Note's label", "Note's content"]
        for note in notes:
            notes_table.add_row([note[1], note[2]])

        notes_table.align = "l"
        print(notes_table)
