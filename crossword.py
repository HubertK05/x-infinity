from typing import List, Tuple
from entry import Entry
from letter import Letter
from util import InvalidCrosswordError


class Crossword:
    def __init__(self, solution_column: int, entries: List[Tuple[int, Entry]]):
        if not entries:
            raise InvalidCrosswordError("Entries cannot be empty")
        if solution_column < 0:
            raise InvalidCrosswordError("Solution column cannot be negative")
        if any(entry[0] < 0 for entry in entries):
            raise InvalidCrosswordError("Entry column cannot be negative")

        self.__solution_column = solution_column
        self.__solution = entries
        self.state = [(offset, [Letter("", False) for _ in range(len(entry.word))]) for offset, entry in entries]

    @property
    def solution(self) -> list[Tuple[int, Entry]]:
        return self.__solution

    @property
    def solution_column(self) -> int:
        return self.__solution_column

    def width(self) -> int:
        return max([entry[0] + len(entry[1].word) for entry in self.__solution])

    def display_str(self) -> str:
        res = ""
        for entry in self.__solution:
            res += " " * entry[0] + f'{entry[1].word}\n'
        return res

    def display_unsolved(self) -> str:
        res = ""
        definitions = ""
        for i, entry in enumerate(self.__solution):
            res += f'{i+1}.' + " " * entry[0] + f'{"_" * len(entry[1].word)}\n'
            definitions += f'{i+1}. {entry[1].definition}\n'
        return res + definitions

    def get_letter(self, row: int, col: int) -> Letter:
        offset = self.__solution[row][0]
        return self.state[row][1][col - offset]

    def set_letter(self, row: int, col: int, letter: int):
        offset = self.__solution[row][0]
        target = self.state[row][1][col - offset]
        if not target.fixed:
            target.letter = letter

    def fix_letter(self, row: int, col: int):
        offset = self.__solution[row][0]
        letter_idx = col - offset
        self.state[row][1][letter_idx].letter = self.__solution[row][1].word[letter_idx]
        self.state[row][1][letter_idx].fixed = True

    def check(self) -> List[Tuple[int, int, bool]]:
        res = []
        for i in range(len(self.__solution)):
            for j in range(len(self.__solution[i][1].word)):
                if self.state[i][1][j].letter:
                    res.append((i, j + self.__solution[i][0], self.state[i][1][j].letter == self.__solution[i][1].word[j]))
        return res
