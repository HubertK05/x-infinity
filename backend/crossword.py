from typing import List, Tuple
from backend.entry import Entry
from backend.letter import Letter
from backend.util import InvalidCrosswordError


class Crossword:
    """
    The Crossword class contains a solution and its current state.

    The solution consists of entries that are the correct answers and the
    column the main solution (the word read from top to bottom formed from all
    entries) is in.

    The current state consists of letters that the user modifies.
    """

    def __init__(self, solution_column: int, entries: List[Tuple[int, Entry]]):
        """
        Initializes the crossword.

        ## Parameters:
        - solution_column: the index of the column (starting from zero) the
        main solution is in.
        - entries: a collection of entries placed from top to bottom
        of the crossword, associated with their offsets - at which cell from
        the left should the entries be placed.
        """
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
        """A list of words from top to bottom in the solution."""
        return self.__solution

    @property
    def solution_column(self) -> int:
        """A column in which there is the crossword's main solution."""
        return self.__solution_column

    def width(self) -> int:
        """The amount of columns the crossword needs."""
        return max([entry[0] + len(entry[1].word) for entry in self.__solution])

    def get_letter(self, row: int, col: int) -> Letter:
        """
        Returns the letter at (`row`, `col`).

        ## Parameters:
        - row - index of an entry in the crossword.
        - col - index of a table item, starting from the first column of the
        crossword (not from the first letter of an entry).

        ## Throws:
        - `IndexError` - if coordinates (`row`, `col`) don't correspond to
        any letter.
        """
        offset = self.__solution[row][0]
        return self.state[row][1][col - offset]

    def set_letter(self, row: int, col: int, letter: str):
        """
        Sets the letter at (`row`, `col`) to `letter`.

        ## Parameters:
        - row - index of an entry in the crossword.
        - col - index of a table item, starting from the first column of the
        crossword (not from the first letter of an entry).
        - letter - the string representation of a letter.

        ## Throws:
        - `IndexError` - if coordinates (`row`, `col`) don't correspond to
        any letter.
        - `InvalidLetterError` - if `letter` consists of multiple characters.
        """
        offset = self.__solution[row][0]
        target = self.state[row][1][col - offset]
        if not target.fixed:
            target.letter = letter

    def fix_letter(self, row: int, col: int):
        """
        Fixes the letter at (`row`, `col`). Fixing means setting the letter to
        the correct letter from the solution and making it immutable.

        ## Parameters:
        - row - index of an entry in the crossword.
        - col - index of a table item, starting from the first column of the
        crossword (not from the first letter of an entry).

        ## Throws:
        - `IndexError` - if coordinates (`row`, `col`) don't correspond to
        any letter.
        """
        offset = self.__solution[row][0]
        letter_idx = col - offset
        self.state[row][1][letter_idx].letter = self.__solution[row][1].word[letter_idx]
        self.state[row][1][letter_idx].fixed = True

    def check(self) -> List[Tuple[int, int, bool]]:
        """
        Checks every letter that has been inserted into the crossword's state.
        Returns for every checked letter its coordinates (`row`, `col`) with
        whether the letter is correct (bool).
        """
        res = []
        for i in range(len(self.__solution)):
            for j in range(len(self.__solution[i][1].word)):
                if self.state[i][1][j].letter:
                    res.append((i, j + self.__solution[i][0], self.state[i][1][j].letter == self.__solution[i][1].word[j]))
        return res
