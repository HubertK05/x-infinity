import PySide6.QtWidgets as widgets
from PySide6.QtGui import QBrush, QColor
from crossword import Crossword


WHITE = QColor(255, 255, 255)
LIGHT_GRAY = QColor(224, 224, 224)
GRAY = QColor(192, 192, 192)
RED = QColor(255, 224, 224)
GREEN = QColor(224, 255, 224)

BACKSPACE_KEY = 16777219
SPACE_KEY = 32
LEFT_ARROW_KEY = 16777234
UP_ARROW_KEY = 16777235
RIGHT_ARROW_KEY = 16777236
DOWN_ARROW_KEY = 16777237


class CrosswordTable(widgets.QTableWidget):
    def __init__(self, crossword: Crossword, parent=None):
        super().__init__(parent)
        self.__backend = crossword
        self.cellDoubleClicked.connect(self.__on_double_clicked)

    def new_crossword(self, crossword: Crossword):
        self.__backend = crossword
        self.clear()
        self.setRowCount(len(crossword.solution))
        self.setColumnCount(crossword.width())
        self.__uncheck()
        self.__refresh_ui()

    def __refresh_ui(self):
        for row, (offset, entry) in enumerate(self.__backend.solution):
            minimum, maximum = offset, offset + len(entry.word) - 1
            for col in range(0, self.__backend.width()):
                item = self.item(row, col)
                if not item:
                    self.setItem(row, col, widgets.QTableWidgetItem(""))
                    item = self.item(row, col)
                if minimum <= col <= maximum:
                    if self.__backend.get_letter(row, col).fixed:
                        item.setBackground(QBrush(GREEN))
                    elif col == self.__backend.solution_column:
                        item.setBackground(QBrush(GRAY))
                    else:
                        item.setBackground(QBrush(LIGHT_GRAY))
                else:
                    item.setBackground(QBrush(WHITE))

    def toggle_check(self):
        if self.__checking:
            self.__uncheck()
        else:
            self.__check()

    def __check(self):
        self.__checking = True
        for row, col, correct in self.__backend.check():
            if correct:
                self.item(row, col).setBackground(QBrush(GREEN))
            else:
                self.item(row, col).setBackground(QBrush(RED))

    def __uncheck(self):
        self.__checking = False
        self.__refresh_ui()

    def keyPressEvent(self, event) -> None:
        if self.__checking:
            return

        indexes = self.selectedIndexes()
        if indexes:
            row, col = indexes[0].row(), indexes[0].column()
        else:
            return

        key = event.key()
        if 65 <= key <= 90:
            self.__type_letter(row, col, chr(key))
        elif key == SPACE_KEY:
            self.__go_to_next(row, col)
        elif key == BACKSPACE_KEY:
            self.__remove_letter(row, col)
        elif key == LEFT_ARROW_KEY:
            self.setCurrentCell(row, max(0, col - 1))
        elif key == RIGHT_ARROW_KEY:
            self.setCurrentCell(row, min(self.columnCount() - 1, col + 1))
        elif key == DOWN_ARROW_KEY:
            self.setCurrentCell(min(self.rowCount() - 1, row + 1), col)
        elif key == UP_ARROW_KEY:
            self.setCurrentCell(max(0, row - 1), col)

    def __type_letter(self, row: int, col: int, key: str):
        minimum = self.__backend.solution[row][0]
        maximum = minimum + len(self.__backend.solution[row][1].word) - 1
        if minimum <= col <= maximum:
            self.__set_letter(row, col, key.lower())
        self.__go_to_next(row, col)

    def __go_to_next(self, row: int, col: int):
        minimum = self.__backend.solution[row][0]
        maximum = minimum + len(self.__backend.solution[row][1].word) - 1
        if col < maximum:
            self.setCurrentCell(row, max(minimum, col + 1))
        elif row < self.rowCount() - 1:
            self.setCurrentCell(row + 1, self.__backend.solution[row + 1][0])

    def __remove_letter(self, row: int, col: int):
        self.__set_letter(row, col, "")

    def __set_letter(self, row: int, col: int, letter: str):
        if not self.__backend.get_letter(row, col).fixed:
            self.__backend.set_letter(row, col, letter)
            self.item(row, col).setText(letter)

    def __on_double_clicked(self, row: int, col: int):
        if self.__checking:
            return

        entries = self.__backend.solution
        minimum = entries[row][0]
        maximum = minimum + len(entries[row][1].word) - 1
        if minimum <= col <= maximum:
            self.__backend.fix_letter(row, col)
            letter = self.__backend.get_letter(row, col)
            self.item(row, col).setText(letter.letter)
            self.item(row, col).setBackground(QBrush(GREEN))
