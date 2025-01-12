from typing import Dict, List
from backend.entry import Entry
from backend.util import ConflictingEntryNameError, InvalidWordlistNameError


class Wordlist:
    """A named collection of entries."""

    def __init__(self, name: str, entries: List[Entry]):
        """
        Initializes a new Wordlist with alphanumeric and non-empty `name` and
        with given `entries`.

        Throws:
        - `InvalidWordlistNameError` - if `name` is empty or it contains
        non-alphanumeric characters.
        """
        if not name:
            raise InvalidWordlistNameError("Wordlist name is empty")
        if not name.isalnum():
            raise InvalidWordlistNameError("Wordlist name contains non-alphanumeric characters")
        self.name = name
        self.__entries: Dict[str, Entry] = {}
        for entry in entries:
            self.__entries[entry.word] = entry

    @property
    def entries(self):
        """A list of all entries."""
        return list(self.__entries.values())

    def get(self, word: str) -> Entry:
        """Returns an entry of a given `word`"""
        return self.__entries.get(word)

    def add(self, entry: Entry):
        """
        Inserts a new entry.

        Throws:
        - `ConflictingEntryNameError` - if `entry` already exists.
        """
        if self.get(entry.word):
            raise ConflictingEntryNameError(f"Entry with name {entry.word} already exists")
        self.__entries[entry.word] = entry

    def remove(self, word: str):
        """
        Removes an entry at a given name from the wordlist. Does nothing if
        the entry with a given `word` does not exist.
        """
        if self.__entries.get(word):
            del self.__entries[word]

    def update(self, entry: Entry):
        """
        Updates entry with a given `entry.word` with new `entry.definition`.

        Throws:
        - `ConflictingEntryNameError` - if entry with a given word doesn't
        exist.
        """
        if self.get(entry.word) is None:
            raise ConflictingEntryNameError(f"Entry with name {entry.word} does not exist")
        self.__entries[entry.word] = entry
