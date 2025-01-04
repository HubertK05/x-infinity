from typing import List, Optional
import PySide6.QtWidgets as widgets

from entry import Entry
from update_entry_ui import Ui_update_entry_dialog
from util import ConflictingEntryNameError, EmptyEntryError
from wordlist import Wordlist
from wordlists_ui import Ui_MainWindow
from new_entry_ui import Ui_new_entry_dialog


class ApplicationWindow(widgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.wordlists: List[Wordlist] = [Wordlist("first", [Entry("word1", "meaning1"), Entry("word2", "meaning2")]), Wordlist("second", [Entry("word3", "meaning3")])]
        self.selected_wordlist: Optional[Wordlist] = None
        self.selected_entry: Optional[Entry] = None

        self.__update_wordlists_ui()
        self.ui.wordlists.itemClicked.connect(self.__on_wordlist_clicked)
        self.ui.wordlist.itemClicked.connect(self.__on_word_clicked)
        self.ui.wordlist_pages.setCurrentIndex(0)
        self.ui.word_pages.setCurrentIndex(0)

        self.ui.new_entry_button.clicked.connect(self.__on_new_entry_dialog)
        self.ui.edit_entry_button.clicked.connect(self.__on_update_entry_dialog)
        self.ui.delete_entry_button.clicked.connect(self.__on_delete_entry)

    def __update_wordlists_ui(self):
        self.ui.wordlists.clear()
        for wordlist in self.wordlists:
            self.ui.wordlists.addItem(wordlist.name)

    def __on_wordlist_clicked(self, item: widgets.QListWidgetItem):
        # TODO: Wordlists shouldn't be filtered and then indexed
        self.selected_wordlist = [wordlist for wordlist in self.wordlists if wordlist.name == item.text()][0]
        self.__update_words_ui()

    def add_entry(self, entry: Entry):
        self.selected_wordlist.add(entry)
        self.__update_words_ui()

    def __update_words_ui(self):
        if self.selected_wordlist:
            self.ui.word_pages.setCurrentIndex(0)
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
        dialog = UpdateEntryDialog(self)
        dialog.exec()

    def __on_delete_entry(self):
        self.selected_wordlist.remove(self.selected_entry.word)
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


def main():
    app = widgets.QApplication([])
    application = ApplicationWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main()
