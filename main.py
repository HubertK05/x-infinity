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
        self.__checking = False

        self.ui.generate_button.clicked.connect(self.__generate_crossword)
        self.ui.select_wordlist_button.clicked.connect(self.__on_select_wordlist)
        self.ui.crossword.cellChanged.connect(self.__on_cell_changed)
        self.ui.crossword.cellDoubleClicked.connect(self.__on_double_clicked)
        self.ui.check_answer_button.clicked.connect(self.__on_check_answer)

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
        if self.__checking:
            return

        entries = self.__crossword.entries
        minimum = entries[row][0]
        maximum = minimum + len(entries[row][1].word) - 1
        if minimum <= col <= maximum:
            letter_idx = col - minimum
            self.__crossword.fix_letter(row, letter_idx)
            letter = self.__crossword.get_letter(row, letter_idx)
            self.ui.crossword.item(row, col).setText(letter.letter)
            self.ui.crossword.item(row, col).setBackground(QBrush(QColor(224, 255, 224)))

    def __on_check_answer(self):
        if self.__checking:
            self.__uncheck()
        else:
            self.__check()

    def __check(self):
        self.__checking = True
        self.ui.crossword.setEditTriggers(widgets.QAbstractItemView.NoEditTriggers)
        for row, col, correct in self.__crossword.check():
            if correct:
                self.ui.crossword.item(row, col).setBackground(QBrush(QColor(224, 255, 224)))
            else:
                self.ui.crossword.item(row, col).setBackground(QBrush(QColor(255, 224, 224)))

    def __uncheck(self):
        self.__checking = False
        self.ui.crossword.setEditTriggers(widgets.QAbstractItemView.AnyKeyPressed)
        self.__repaint_crossword()

    def __generate_crossword(self):
        if not self.__selected_wordlist:
            widgets.QMessageBox.critical(self, "Error", "No wordlist selected")
            return
        self.ui.title.setText(f"Crossword from wordlist {self.__selected_wordlist.name}")
        try:
            gen = CrosswordGenerator()
            gen.entries = self.__selected_wordlist.entries
            self.__crossword = gen.generate(self.ui.solution_input.text())
            self.__refresh_crossword()
            self.__update_definition_ui()
        except CrosswordGenerationError as e:
            widgets.QMessageBox.critical(self, "Error", str(e))
            return

    def __refresh_crossword(self):
        self.__uncheck()
        self.ui.crossword_pages.setCurrentIndex(1)
        entries: List[Tuple[int, Entry]] = self.__crossword.entries
        width = self.__crossword.width()
        self.ui.crossword.clear()
        self.ui.crossword.setRowCount(len(entries))
        self.ui.crossword.setColumnCount(width)
        self.__repaint_crossword()

    def __repaint_crossword(self):
        for row, (offset, entry) in enumerate(self.__crossword.entries):
            minimum, maximum = offset, offset + len(entry.word) - 1
            for col in range(0, self.__crossword.width()):
                item = self.ui.crossword.item(row, col)
                if not item:
                    self.ui.crossword.setItem(row, col, widgets.QTableWidgetItem(""))
                    item = self.ui.crossword.item(row, col)
                if minimum <= col <= maximum:
                    if self.__crossword.get_letter(row, col - minimum).fixed:
                        item.setBackground(QBrush(QColor(224, 255, 224)))
                    elif col == self.__crossword.solution_column:
                        item.setBackground(QBrush(QColor(192, 192, 192)))
                    else:
                        item.setBackground(QBrush(QColor(224, 224, 224)))
                else:
                    item.setBackground(QBrush(QColor(255, 255, 255)))

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
