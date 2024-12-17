from entry import Entry


class Crossword:
    def __init__(self, solution_column: int, entries: list[(int, Entry)]):
        self.__solution_column = solution_column
        self.__entries = entries

    @property
    def entries(self) -> list[(int, Entry)]:
        return self.__entries

    @property
    def solution_column(self) -> int:
        return self.__solution_column
