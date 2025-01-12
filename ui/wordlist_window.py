import random
from typing import List, Optional
import PySide6.QtWidgets as widgets
from PySide6.QtGui import QCloseEvent

from backend.entry import Entry
from ui_widgets.new_wordlist_ui import Ui_new_wordlist_dialog
from ui_widgets.update_entry_ui import Ui_update_entry_dialog
from ui_widgets.update_wordlist_ui import Ui_update_wordlist_dialog
from backend.util import ConflictingEntryNameError, EmptyEntryError, InvalidWordlistNameError
from backend.wordlist import Wordlist
from backend.wordlist_file_access import WordlistFileAccess
from ui_widgets.wordlists_ui import Ui_MainWindow
from ui_widgets.new_entry_ui import Ui_new_entry_dialog


class WordlistWindow(widgets.QMainWindow):
    """A window in which the user manages their wordlists and entries."""

    def __init__(self, parent=None):
        """Initializes the wordlist selection window."""
        super().__init__(parent)

        self.wordlists: List[Wordlist] = []
        self.selected_wordlist: Optional[Wordlist] = None
        self.selected_entry: Optional[Entry] = None
        self.db = WordlistFileAccess()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__update_wordlists_ui()
        self.ui.wordlists.itemClicked.connect(self.__on_wordlist_clicked)
        self.ui.wordlist.itemClicked.connect(self.__on_word_clicked)

        self.ui.new_entry_button.clicked.connect(self.__on_new_entry_dialog)
        self.ui.edit_entry_button.clicked.connect(self.__on_update_entry_dialog)
        self.ui.delete_entry_button.clicked.connect(self.__on_delete_entry)
        self.ui.new_wordlist_button.clicked.connect(self.__on_new_wordlist_dialog)
        self.ui.update_wordlist_button.clicked.connect(self.__on_update_wordlist_dialog)
        self.ui.delete_wordlist_button.clicked.connect(self.__delete_wordlist)
        self.ui.use_wordlist_button.clicked.connect(self.__on_use_wordlist)
        self.ui.generate_wordlist_button.clicked.connect(self.__on_generate_wordlist)
        self.ui.generate_definitions_button.clicked.connect(self.__on_generate_definitions)

    def create_wordlist(self, name: str):
        """Creates a new empty wordlist with a given name."""
        self.db.set_wordlist(Wordlist(name, []))
        self.__update_wordlists_ui()

    def rename_wordlist(self, old_name: str, new_name: str):
        """Renames a given wordlist."""
        self.db.rename_wordlist(old_name, new_name)
        self.__update_wordlists_ui()

    def __delete_wordlist(self):
        """
        Deletes the selected wordlist, alongside with its file and all its
        entries.
        """
        self.selected_entry = None
        self.selected_wordlist = None
        self.db.delete_wordlist(self.selected_wordlist.name)
        self.__update_wordlists_ui()

    def __on_use_wordlist(self):
        """Uses the selected wordlist for crosswords. Closes this window."""
        self.parent().selected_wordlist = self.selected_wordlist
        self.parent().ui.selected_wordlist_label.setText(f"Selected wordlist: {self.selected_wordlist.name}")
        self.close()

    def __on_new_wordlist_dialog(self):
        """Opens the wordlist creation dialog."""
        dialog = CreateWordlistDialog(self)
        dialog.exec()

    def __on_update_wordlist_dialog(self):
        """Opens the wordlist rename dialog."""
        dialog = UpdateWordlistDialog(self.selected_wordlist.name, self)
        dialog.exec()

    def __update_wordlists_ui(self):
        """
        Refreshes the list of wordlists. Also hides wordlist content and
        entry content.
        """
        self.ui.wordlist_pages.setCurrentIndex(0)
        self.ui.word_pages.setCurrentIndex(0)
        self.ui.wordlists.clear()
        for name in self.db.list_wordlists():
            self.ui.wordlists.addItem(name)

    def __on_wordlist_clicked(self, item: widgets.QListWidgetItem):
        """Selects a given wordlist and shows its options."""
        self.selected_wordlist = self.db.get_wordlist(item.text())
        self.__update_words_ui()

    def add_entry(self, entry: Entry):
        """Adds the entry to the selected wordlist."""
        self.selected_wordlist.add(entry)
        self.db.set_wordlist(self.selected_wordlist)
        self.__update_words_ui()

    def __update_words_ui(self):
        """
        Refreshes the contents of the wordlist in the UI. Also hides entry
        content.
        """
        self.ui.word_pages.setCurrentIndex(0)
        if self.selected_wordlist:
            self.ui.wordlist_pages.setCurrentIndex(1)
            self.ui.wordlist.clear()
            for entry in self.selected_wordlist.entries:
                self.ui.wordlist.addItem(entry.word)
        else:
            self.ui.wordlist_pages.setCurrentIndex(0)

    def __on_word_clicked(self, item: widgets.QListWidgetItem):
        """Selects a given entry and shows its options."""
        self.selected_entry = self.selected_wordlist.get(item.text())
        self.__update_entry_ui()

    def update_entry(self, entry: Entry):
        """Sets the selected entry in the selected wordlist to a new entry."""
        self.selected_wordlist.update(entry)
        self.db.set_wordlist(self.selected_wordlist)
        self.selected_entry = entry
        self.__update_entry_ui()

    def __update_entry_ui(self):
        """Refreshes the content of a single entry."""
        if self.selected_entry:
            entry = self.selected_entry
            self.ui.word_label.setText(entry.word)
            self.ui.definition_label.setText(entry.definition)
            self.ui.word_pages.setCurrentIndex(1)
        else:
            self.ui.word_pages.setCurrentIndex(0)

    def __on_new_entry_dialog(self):
        """Opens the new entry dialog."""
        dialog = NewEntryDialog(self)
        dialog.exec()

    def __on_update_entry_dialog(self):
        """Opens the update entry dialog."""
        dialog = UpdateEntryDialog(self.selected_entry.word, self)
        dialog.exec()

    def __on_delete_entry(self):
        """Deletes a given entry from the selected wordlist."""
        self.selected_wordlist.remove(self.selected_entry.word)
        self.db.set_wordlist(self.selected_wordlist)
        self.selected_entry = None
        self.__update_words_ui()

    def __on_generate_wordlist(self):
        """
        Automatically generates a new wordlist of 100 randomly selected
        words with their definitions.
        """
        entries = self.db.get_full_data()
        wordlist = Wordlist("Generated", random.sample(entries, 100))
        self.db.set_wordlist(wordlist)
        self.__update_wordlists_ui()

    def __on_generate_definitions(self):
        """
        Attempts to automatically complete words with their definitions. This
        doesn't guarantee that every word gets its definition.
        """
        words = set([entry.word for entry in self.selected_wordlist.entries])
        entries = self.db.get_full_data()
        matching_entries = [entry for entry in entries if entry.word in words]
        for entry in matching_entries:
            self.selected_wordlist.update(entry)
        self.selected_entry = None
        self.db.set_wordlist(self.selected_wordlist)
        self.__update_entry_ui()

    def closeEvent(self, event: QCloseEvent):
        self.parent().ui.select_wordlist_button.setEnabled(True)


class NewEntryDialog(widgets.QDialog):
    """A dialog window used in entry creation."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_entry_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        """Creates a new entry."""
        try:
            entry = Entry(self.ui.word.text(), self.ui.definition.text())
            self.parent().add_entry(entry)
        except (EmptyEntryError, ConflictingEntryNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))


class UpdateEntryDialog(widgets.QDialog):
    """A dialog window used in entry update."""

    def __init__(self, word: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_update_entry_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)
        self.ui.name.setText(f"Update entry \"{word}\"")

    def __on_accepted(self):
        """Updates the entry's definition."""
        try:
            name = self.parent().selected_entry.word
            definition = self.ui.definition.text()
            entry = Entry(name, definition)
            self.parent().update_entry(entry)
        except (EmptyEntryError, ConflictingEntryNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))


class CreateWordlistDialog(widgets.QDialog):
    """A dialog window used in wordlist creation."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_new_wordlist_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)

    def __on_accepted(self):
        """Creates a new wordlist."""
        try:
            self.parent().create_wordlist(self.ui.name.text())
        except (ConflictingEntryNameError, InvalidWordlistNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))


class UpdateWordlistDialog(widgets.QDialog):
    """A dialog window used in wordlist update."""

    def __init__(self, name: str, parent=None):
        super().__init__(parent)
        self.ui = Ui_update_wordlist_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.__on_accepted)
        self.ui.old_name.setText(f"Update wordlist \"{name}\"")

    def __on_accepted(self):
        """Updates the wordlist's name."""
        try:
            self.parent().rename_wordlist(self.parent().selected_wordlist.name, self.ui.new_name.text())
        except (ConflictingEntryNameError, InvalidWordlistNameError) as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
