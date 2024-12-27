from crossword import Crossword
from entry import Entry
import random

from util import CrosswordGenerationError


class CrosswordGenerator:
    def __init__(self):
        self.entries: list[Entry] = []

    def generate(self, solution: str | None = None) -> Crossword:
        """Generates the crossword based on entries given to the generator"""
        matching: list[tuple[int, Entry]] = self._find_random_matching(solution if solution else random.choose(self.entries).word)
        solution_column = max(matching, key=lambda entry: entry[0])[0]
        matching = [(solution_column - pos, entry) for pos, entry in matching]
        return Crossword(solution_column, matching)

    def _find_random_matching(self, solution) -> list[tuple[int, Entry]]:
        res: list[tuple[int, Entry]] = []
        for letter in solution:
            entries: list[Entry] = self.entries[:]
            random.shuffle(entries)
            found = False
            for entry in entries:
                word = entry.word
                word_in_result = next((entry for entry in res[:] if entry[1].word == word), None)
                if letter in word and not word_in_result and word != solution:
                    all_positions = find_all(entry.word, letter)
                    res.append((random.choice(all_positions), entry))
                    found = True
                    break
            if not found:
                raise CrosswordGenerationError("Cannot create crossword with a given word list")
        return res


def find_all(word: str, letter: str) -> list[int]:
    res = []
    for i, word_letter in enumerate(word):
        if letter == word_letter:
            res.append(i)
    return res
