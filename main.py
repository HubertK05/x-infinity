from typing import List, Optional, Tuple
import PySide6.QtWidgets as widgets
from PySide6.QtGui import QBrush, QColor
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

        self.__selected_wordlist: Optional[Wordlist] = None
        self.__crossword = None
        self.ui.generate_button.clicked.connect(self.__generate_crossword)
        self.ui.pushButton.clicked.connect(self.__on_select_wordlist)
        self.ui.crossword.cellChanged.connect(self.__on_cell_changed)
        self.ui.crossword.cellDoubleClicked.connect(self.__on_double_clicked)

    @property
    def selected_wordlist(self):
        return self.__selected_wordlist

    @selected_wordlist.setter
    def selected_wordlist(self, wordlist):
        self.__selected_wordlist = wordlist

    def __on_cell_changed(self, row: int, col: int):
        entries = self.__crossword.entries
        minimum = entries[row][0]
        maximum = minimum + len(entries[row][1].word) - 1
        text = self.ui.crossword.item(row, col).text()

        if minimum <= col <= maximum:
            letter_idx = col - minimum
            target_letter = self.__crossword.get_letter(row, letter_idx)
            if target_letter.fixed and target_letter.letter != text:
                self.ui.crossword.item(row, col).setText(target_letter.letter)
                return
            elif text:
                self.__crossword.set_letter(row, letter_idx, text[-1])

        if not text:
            return
        if col < minimum or maximum < col:
            self.ui.crossword.item(row, col).setText("")
        else:
            self.ui.crossword.item(row, col).setText(text[-1])

        if col < minimum:
            self.ui.crossword.setCurrentCell(row, minimum)
        elif minimum <= col < maximum:
            self.ui.crossword.setCurrentCell(row, col + 1)
        else:
            if row < len(entries) - 1:
                self.ui.crossword.setCurrentCell(row + 1, entries[row + 1][0])

    def __on_double_clicked(self, row: int, col: int):
        entries = self.__crossword.entries
        minimum = entries[row][0]
        maximum = minimum + len(entries[row][1].word) - 1
        if minimum <= col <= maximum:
            letter_idx = col - minimum
            self.__crossword.fix_letter(row, letter_idx)
            letter = self.__crossword.get_letter(row, letter_idx)
            self.ui.crossword.item(row, col).setText(letter.letter)
            self.ui.crossword.item(row, col).setBackground(QBrush(QColor(224, 255, 224)))

    def __generate_crossword(self):
        if not self.__selected_wordlist:
            widgets.QMessageBox.critical(self, "Error", "No wordlist selected")
            return
        self.ui.title.setText(f"Crossword from wordlist {self.__selected_wordlist.name}")
        try:
            gen = CrosswordGenerator()
            gen.entries = self.__selected_wordlist.entries
            self.__crossword = gen.generate(self.ui.solution_input.text())
            self.__update_crossword_ui()
            self.__update_definition_ui()
        except CrosswordGenerationError as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
            return

    def __update_crossword_ui(self):
        entries: List[Tuple[int, Entry]] = self.__crossword.entries
        width = self.__crossword.width()
        self.ui.crossword.clear()
        self.ui.crossword.setRowCount(len(entries))
        self.ui.crossword.setColumnCount(width)

        for row, (offset, entry) in enumerate(entries):
            minimum, maximum = offset, offset + len(entry.word) - 1
            for col in range(0, width):
                item = widgets.QTableWidgetItem("")
                if minimum <= col <= maximum:
                    item.setBackground(QBrush(QColor(224, 224, 224)))
                if col == self.__crossword.solution_column:
                    item.setBackground(QBrush(QColor(192, 192, 192)))
                self.ui.crossword.setItem(row, col, item)

    def __update_definition_ui(self):
        self.ui.definitions.clear()
        entries: List[Tuple[int, Entry]] = self.__crossword.entries
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
