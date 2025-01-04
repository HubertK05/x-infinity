from typing import List, Self
from entry import Entry
from util import ConflictingEntryNameError, EmptyWordlistNameError


class Wordlist:
    def __init__(self, name, entries: List[Entry]):
        if not name:
            raise EmptyWordlistNameError("Wordlist name is empty")
        self.name = name
        self.__entries = {}
        for entry in entries:
            self.__entries[entry.word] = entry.definition

    def __eq__(self, other: Self):
        return self.name == other.name and sorted(self.entries) == sorted(other.entries)

    @property
    def entries(self):
        return [Entry(word, definition) for word, definition in self.__entries.items()]

    def get(self, word) -> Entry:
        definition = self.__entries.get(word)
        if definition is None:
            return None
        return Entry(word, definition)

    def add(self, entry: Entry):
        if self.get(entry.word):
            raise ConflictingEntryNameError(f"Entry with name {entry.word} already exists")
        self.__entries[entry.word] = entry.definition

    def remove(self, name: str):
        if self.__entries.get(name):
            del self.__entries[name]

    def update(self, entry: Entry):
        if self.get(entry.word) is None:
            raise ConflictingEntryNameError(f"Entry with name {entry.word} does not exist")
        self.__entries[entry.word] = entry.definition
