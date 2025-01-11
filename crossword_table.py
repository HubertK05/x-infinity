import PySide6.QtWidgets as widgets
from PySide6.QtGui import QBrush, QColor
from crossword import Crossword


class CrosswordTable(widgets.QTableWidget):
    def __init__(self, crossword: Crossword, parent=None):
        super().__init__(parent)
        self.__backend = crossword
        self.cellDoubleClicked.connect(self.__on_double_clicked)

    def new_crossword(self, crossword: Crossword):
        self.__backend = crossword
        self.clear()
        self.setRowCount(len(crossword.entries))
        self.setColumnCount(crossword.width())
        self.__uncheck()
        self.__refresh_ui()

    def __refresh_ui(self):
        for row, (offset, entry) in enumerate(self.__backend.entries):
            minimum, maximum = offset, offset + len(entry.word) - 1
            for col in range(0, self.__backend.width()):
                item = self.item(row, col)
                if not item:
                    self.setItem(row, col, widgets.QTableWidgetItem(""))
                    item = self.item(row, col)
                if minimum <= col <= maximum:
                    if self.__backend.get_letter(row, col - minimum).fixed:
                        item.setBackground(QBrush(QColor(224, 255, 224)))
                    elif col == self.__backend.solution_column:
                        item.setBackground(QBrush(QColor(192, 192, 192)))
                    else:
                        item.setBackground(QBrush(QColor(224, 224, 224)))
                else:
                    item.setBackground(QBrush(QColor(255, 255, 255)))

    def toggle_check(self):
        if self.__checking:
            self.__uncheck()
        else:
            self.__check()

    def __check(self):
        self.__checking = True
        for row, col, correct in self.__backend.check():
            if correct:
                self.item(row, col).setBackground(QBrush(QColor(224, 255, 224)))
            else:
                self.item(row, col).setBackground(QBrush(QColor(255, 224, 224)))

    def __uncheck(self):
        self.__checking = False
        self.__refresh_ui()

    def keyPressEvent(self, event) -> None:
        if self.__checking or not 65 <= event.key() <= 90:
            return

        indexes = self.selectedIndexes()
        if indexes:
            row, col = indexes[0].row(), indexes[0].column()
            minimum = self.__backend.entries[row][0]
            maximum = minimum + len(self.__backend.entries[row][1].word) - 1
            if minimum <= col <= maximum and not self.__backend.get_letter(row, col - minimum).fixed:
                letter = chr(event.key() + 32)
                self.item(row, col).setText(letter)
                self.__backend.set_letter(row, col - minimum, letter)
            if col < maximum:
                self.setCurrentCell(row, max(minimum, col + 1))
            elif row < self.rowCount() - 1:
                self.setCurrentCell(row + 1, self.__backend.entries[row + 1][0])

    def __on_double_clicked(self, row: int, col: int):
        if self.__checking:
            return

        entries = self.__backend.entries
        minimum = entries[row][0]
        maximum = minimum + len(entries[row][1].word) - 1
        if minimum <= col <= maximum:
            letter_idx = col - minimum
            self.__backend.fix_letter(row, letter_idx)
            letter = self.__backend.get_letter(row, letter_idx)
            self.item(row, col).setText(letter.letter)
            self.item(row, col).setBackground(QBrush(QColor(224, 255, 224)))
