from typing import Dict, List
from entry import Entry
from util import ConflictingEntryNameError, InvalidWordlistNameError


class Wordlist:
    def __init__(self, name: str, entries: List[Entry]):
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
        return list(self.__entries.values())

    def get(self, word: str) -> Entry:
        return self.__entries.get(word)

    def add(self, entry: Entry):
        if self.get(entry.word):
            raise ConflictingEntryNameError(f"Entry with name {entry.word} already exists")
        self.__entries[entry.word] = entry

    def remove(self, name: str):
        if self.__entries.get(name):
            del self.__entries[name]

    def update(self, entry: Entry):
        if self.get(entry.word) is None:
            raise ConflictingEntryNameError(f"Entry with name {entry.word} does not exist")
        self.__entries[entry.word] = entry
