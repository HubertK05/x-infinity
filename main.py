import PySide6.QtWidgets as widgets

from entry import Entry
from wordlists import Ui_MainWindow


class ApplicationWindow(widgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # TODO: Add Wordlist class, with name and entries
        self.wordlists = [("first", [Entry("word1", "meaning1"), Entry("word2", "meaning2")]), ("second", [Entry("word3", "meaning3")])]
        self.selected_wordlist = None
        self.selected_entry = None

        self.__update_wordlists_ui()
        self.ui.wordlists.itemClicked.connect(self.__on_wordlist_clicked)
        self.ui.wordlist.itemClicked.connect(self.__on_word_clicked)
        self.ui.wordlist_pages.setCurrentIndex(0)
        self.ui.word_pages.setCurrentIndex(0)

    def __update_wordlists_ui(self):
        self.ui.wordlists.clear()
        for wordlist in self.wordlists:
            # TODO: Wordlist class should have a name attribute, not indexing
            self.ui.wordlists.addItem(wordlist[0])

    def __on_wordlist_clicked(self, item):
        self.selected_wordlist = [wordlist for wordlist in self.wordlists if wordlist[0] == item.text()][0]
        entries = self.selected_wordlist[1]
        self.__update_words_ui(entries)

    def __update_words_ui(self, entries):
        self.ui.word_pages.setCurrentIndex(0)
        self.ui.wordlist_pages.setCurrentIndex(1)
        self.ui.wordlist.clear()
        for entry in entries:
            self.ui.wordlist.addItem(entry.word)

    def __on_word_clicked(self, item):
        self.selected_entry = [entry for entry in self.selected_wordlist[1] if entry.word == item.text()][0]
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
