from util import ConflictingEntryNameError
from wordlist import Wordlist


class WordlistCache:
    def __init__(self):
        self.__wordlists = {}

    @property
    def wordlists(self):
        return [Wordlist(name, entries) for name, entries in self.__wordlists.items()]

    def get(self, name: str) -> Wordlist:
        if name in self.__wordlists:
            return Wordlist(name, self.__wordlists[name])

    def add(self, wordlist: Wordlist):
        if wordlist.name in self.__wordlists:
            raise ConflictingEntryNameError(f"Wordlist with name {wordlist.name} already exists")
        self.__wordlists[wordlist.name] = wordlist.entries

    def update(self, old_name: str, new_name: str):
        if old_name not in self.__wordlists:
            raise ConflictingEntryNameError(f"Wordlist with name {old_name} does not exist")
        if new_name in self.__wordlists:
            raise ConflictingEntryNameError(f"Wordlist with name {new_name} already exists")
        self.__wordlists[new_name] = self.__wordlists.pop(old_name)

    def remove(self, name: str):
        if name in self.__wordlists:
            del self.__wordlists[name]
