from typing import Self
from util import InvalidLetterError


class Letter:
    def __init__(self, letter: str, fixed: bool):
        if len(letter) > 1:
            raise InvalidLetterError(f"'{letter}' is not a single character")
        self.__letter = letter
        self.fixed = fixed

    def __eq__(self, other: Self):
        return self.letter == other.letter and self.fixed == other.fixed

    @property
    def letter(self):
        return self.__letter

    @letter.setter
    def letter(self, letter: str):
        if len(letter) > 1:
            raise InvalidLetterError(f"'{letter}' is not a single character")
        self.__letter = letter
