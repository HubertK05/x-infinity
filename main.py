from typing import List, Optional, Tuple
import PySide6.QtWidgets as widgets
from crossword_generator import CrosswordGenerator
from crosswords_ui import Ui_MainWindow
from entry import Entry
from util import CrosswordGenerationError
from wordlist import Wordlist
from wordlist_window import WordlistWindow


class CrosswordWindow(widgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.selected_wordlist: Optional[Wordlist] = None

        self.ui.generate_button.clicked.connect(self.__generate_crossword)
        self.ui.select_wordlist_button.clicked.connect(self.__on_select_wordlist)
        self.ui.check_answer_button.clicked.connect(self.__on_check_answer)

    def __on_check_answer(self):
        self.ui.crossword.toggle_check()

    def __generate_crossword(self):
        if not self.selected_wordlist:
            widgets.QMessageBox.critical(self, "Error", "No wordlist selected")
            return
        self.ui.title.setText(f"Crossword from wordlist {self.selected_wordlist.name}")
        try:
            gen = CrosswordGenerator()
            gen.entries = self.selected_wordlist.entries
            crossword = gen.generate(self.ui.solution_input.text())
            self.ui.crossword.new_crossword(crossword)
            self.__update_definition_ui(crossword.solution)
        except CrosswordGenerationError as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
            return

    def __update_definition_ui(self, entries: List[Tuple[int, Entry]]):
        self.ui.definitions.clear()
        self.ui.definitions.addItems([f"{i + 1}. {entry.definition}" for i, (_, entry) in enumerate(entries)])

    def __on_select_wordlist(self):
        self.wordlist_window = WordlistWindow(self)
        self.wordlist_window.show()


def main():
    app = widgets.QApplication([])
    application = CrosswordWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main()
