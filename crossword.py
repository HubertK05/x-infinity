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

    def display_str(self) -> str:
        res = ""
        for entry in self.__entries:
            res += " " * entry[0] + f'{entry[1].word}\n'
        return res

    def display_unsolved(self) -> str:
        res = ""
        definitions = ""
        for i, entry in enumerate(self.__entries):
            res += f'{i+1}.' + " " * entry[0] + f'{"_" * len(entry[1].word)}\n'
            definitions += f'{i+1}. {entry[1].definition}\n'
        return res + definitions
