from typing import List, Optional
import PySide6.QtWidgets as widgets

from entry import Entry
from wordlist import Wordlist
from wordlists import Ui_MainWindow


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

    def __update_wordlists_ui(self):
        self.ui.wordlists.clear()
        for wordlist in self.wordlists:
            self.ui.wordlists.addItem(wordlist.name)

    def __on_wordlist_clicked(self, item: widgets.QListWidgetItem):
        # TODO: Wordlists shouldn't be filtered and then indexed
        self.selected_wordlist = [wordlist for wordlist in self.wordlists if wordlist.name == item.text()][0]
        entries = self.selected_wordlist.entries
        self.__update_words_ui(entries)

    def __update_words_ui(self, entries):
        self.ui.word_pages.setCurrentIndex(0)
        self.ui.wordlist_pages.setCurrentIndex(1)
        self.ui.wordlist.clear()
        for entry in entries:
            self.ui.wordlist.addItem(entry.word)

    def __on_word_clicked(self, item: widgets.QListWidgetItem):
        self.selected_entry = self.selected_wordlist.get(item.text())
        self.__update_entry_ui(self.selected_entry)

    def __update_entry_ui(self, entry: Entry):
        self.ui.word_pages.setCurrentIndex(1)
        self.ui.entry.clear()
        self.ui.entry.addItem(entry.word)
        self.ui.entry.addItem(entry.definition)


def main():
    app = widgets.QApplication([])
    application = ApplicationWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main()
