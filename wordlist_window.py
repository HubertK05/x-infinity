from typing import List, Optional
import PySide6.QtWidgets as widgets

from entry import Entry
from new_wordlist_ui import Ui_new_wordlist_dialog
from update_entry_ui import Ui_update_entry_dialog
from update_wordlist_ui import Ui_update_wordlist_dialog
from util import ConflictingEntryNameError, EmptyEntryError, EmptyWordlistNameError
from wordlist import Wordlist
from wordlist_database import WordlistDatabase
from wordlists_ui import Ui_MainWindow
from new_entry_ui import Ui_new_entry_dialog


class WordlistWindow(widgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.wordlists: List[Wordlist] = []
        self.selected_wordlist: Optional[Wordlist] = None
        self.selected_entry: Optional[Entry] = None
        self.db = WordlistDatabase()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__update_wordlists_ui()
        self.ui.wordlists.itemClicked.connect(self.__on_wordlist_clicked)
        self.ui.wordlist.itemClicked.connect(self.__on_word_clicked)
        self.ui.wordlist_pages.setCurrentIndex(0)
        self.ui.word_pages.setCurrentIndex(0)

        self.ui.new_entry_button.clicked.connect(self.__on_new_entry_dialog)
        self.ui.edit_entry_button.clicked.connect(self.__on_update_entry_dialog)
        self.ui.delete_entry_button.clicked.connect(self.__on_delete_entry)
        self.ui.new_wordlist_button.clicked.connect(self.__on_new_wordlist_dialog)
        self.ui.update_wordlist_button.clicked.connect(self.__on_update_wordlist_dialog)
        self.ui.delete_wordlist_button.clicked.connect(self.__delete_wordlist)

    def create_wordlist(self, name: str):
        self.db.create(name)
        self.__update_wordlists_ui()

    def update_wordlist_name(self, old_name: str, wordlist: Wordlist):
        self.db.update(old_name, wordlist)
        self.__update_wordlists_ui()

    def __persist_wordlist(self):
        self.db.update(self.selected_wordlist.name, self.selected_wordlist)

    def __delete_wordlist(self):
        self.db.delete(self.selected_wordlist.name)
        self.selected_entry = None
        self.selected_wordlist = None
        self.__update_entry_ui()
        self.__update_words_ui()
        self.__update_wordlists_ui()

    def __save_wordlist(self, name: str):
        pass

    def __on_new_wordlist_dialog(self):
        dialog = CreateWordlistDialog(self)
        dialog.exec()

    def __on_update_wordlist_dialog(self):
        dialog = UpdateWordlistDialog(self)
        dialog.exec()

    def __update_wordlists_ui(self):
        self.ui.wordlist_pages.setCurrentIndex(0)
        self.ui.wordlists.clear()
        for name in self.db.list_names():
            self.ui.wordlists.addItem(name)

    def __on_wordlist_clicked(self, item: widgets.QListWidgetItem):
        # TODO: Wordlists shouldn't be filtered and then indexed
        self.selected_wordlist = self.db.get(item.text())
        self.__update_words_ui()

    def add_entry(self, entry: Entry):
        self.selected_wordlist.add(entry)
        self.__persist_wordlist()
        self.__update_words_ui()

    def __update_words_ui(self):
        self.ui.word_pages.setCurrentIndex(0)
        if self.selected_wordlist:
            self.ui.wordlist_pages.setCurrentIndex(1)
            self.ui.wordlist.clear()
            for entry in self.selected_wordlist.entries:
                self.ui.wordlist.addItem(entry.word)
        else:
            self.ui.wordlist_pages.setCurrentIndex(0)

    def __on_word_clicked(self, item: widgets.QListWidgetItem):
        self.selected_entry = self.selected_wordlist.get(item.text())
        self.__update_entry_ui()

    def update_entry(self, entry: Entry):
        self.selected_wordlist.update(entry)
        self.__persist_wordlist()
        self.selected_entry = entry
        self.__update_entry_ui()

    def __update_entry_ui(self):
        if self.selected_entry:
            self.ui.word_pages.setCurrentIndex(1)
            self.ui.entry.clear()
            entry = self.selected_entry
            self.ui.entry.addItem(entry.word)
            self.ui.entry.addItem(entry.definition)
        else:
            self.ui.word_pages.setCurrentIndex(0)

    def __on_new_entry_dialog(self):
        dialog = NewEntryDialog(self)
        dialog.exec()

    def __on_update_entry_dialog(self):
        # TODO: UpdateEntryDialog has a placeholder for entry name. Remove it.
        dialog = UpdateEntryDialog(self)
        dialog.exec()

    def __on_delete_entry(self):
        self.selected_wordlist.remove(self.selected_entry.word)
        self.__persist_wordlist()
        self.selected_entry = None
        self.__update_words_ui()
        self.__update_entry_ui()


class NewEntryDialog(widgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_entry_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        try:
            entry = Entry(self.ui.word.text(), self.ui.definition.text())
            self.parent().add_entry(entry)
        except (EmptyEntryError, ConflictingEntryNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))


class UpdateEntryDialog(widgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_update_entry_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        try:
            name = self.parent().selected_entry.word
            definition = self.ui.definition.text()
            entry = Entry(name, definition)
            self.parent().update_entry(entry)
        except (EmptyEntryError, ConflictingEntryNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))


class CreateWordlistDialog(widgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_wordlist_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        try:
            self.parent().create_wordlist(self.ui.name.text())
        except (ConflictingEntryNameError, EmptyWordlistNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))


class UpdateWordlistDialog(widgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_update_wordlist_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        try:
            new_wordlist = Wordlist(self.ui.new_name.text(), self.parent().selected_wordlist.entries)
            self.parent().update_wordlist(self.parent().selected_wordlist.name, new_wordlist)
        except (ConflictingEntryNameError, EmptyWordlistNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
