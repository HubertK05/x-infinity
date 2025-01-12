import random
from typing import List, Tuple, Optional

from backend.crossword import Crossword
from backend.entry import Entry
from backend.util import CrosswordGenerationError


class CrosswordGenerator:
    """A class that takes in entries and generates crosswords based on them"""

    def __init__(self):
        self.entries: List[Entry] = []

    def generate(self, solution: Optional[str] = None) -> Crossword:
        """
        Generates the crossword based on entries given to the generator.
        The generator chooses the main solution and words from entries at
        random. If the `solution` is given, the main solution is forced
        to be that word.

        ## Parameters:
        - solution: If given, this is the main solution to the crossword.

        ## Throws:
        - `CrosswordGenerationError` - if an attempt to create the crossword
        fails.
        """
        if solution:
            attempts = [solution]
        else:
            words = [entry.word for entry in self.entries[:]]
            random.shuffle(words)
            attempts = words

        matching = None
        for attempt in attempts:
            matching = self._find_random_matching(attempt)
            if matching:
                break
        if not matching:
            raise CrosswordGenerationError("Cannot create crossword with the given word list")

        solution_column = max(matching, key=lambda entry: entry[0])[0]
        adjusted_matching = [(solution_column - pos, entry) for pos, entry in matching]
        return Crossword(solution_column, adjusted_matching)

    def _find_random_matching(self, solution: str) -> Optional[List[Tuple[int, Entry]]]:
        """
        Attempts to find distinct matching words to a given `solution` at
        random. A word is matching if it has a given letter of the solution.
        """
        result: List[Tuple[int, Entry]] = []
        for letter in solution:
            entries_copy = self.entries[:]
            random.shuffle(entries_copy)
            found = False
            for entry in entries_copy:
                if self._can_add_entry(entry, letter, solution, result):
                    all_positions = self.__find_all(entry.word, letter)
                    result.append((random.choice(all_positions), entry))
                    found = True
                    break
            if not found:
                return None
        return result

    def _can_add_entry(self, entry: Entry, letter: str, solution: str, result: List[Tuple[int, Entry]]) -> bool:
        """Checks if an entry is distinct and matching the solution."""
        word = entry.word
        word_in_result = any(existing_entry.word == word for _, existing_entry in result)
        return letter in word and not word_in_result and word != solution

    def __find_all(self, word: str, letter: str) -> List[int]:
        """Finds all indexes, where `letter` occurs in `word`."""
        return [i for i, word_letter in enumerate(word) if letter == word_letter]
