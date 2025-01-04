from util import ConflictingEntryNameError, EmptyWordlistNameError
from wordlist import Wordlist
from wordlist_cache import WordlistCache
from wordlist_file_access import WordlistFileAccess


class WordlistDatabase:
    def __init__(self):
        self.__file_access = WordlistFileAccess()
        self.__cache = WordlistCache()

    def create(self, name: str):
        if name in self.list_names():
            raise ConflictingEntryNameError(f"Wordlist with name {name} already exists")
        if not name:
            raise EmptyWordlistNameError("Wordlist name is empty")
        self.__file_access.set_wordlist(name, [])
        self.__cache.add(Wordlist(name, []))

    def get(self, name: str) -> Wordlist:
        res = self.__cache.get(name)
        if not res:
            wordlist = Wordlist(name, self.__file_access.get_wordlist(name))
            self.__cache.add(wordlist)
            return wordlist
        else:
            return res

    def update(self, old_name: str, wordlist: Wordlist):
        if old_name not in self.list_names():
            raise ConflictingEntryNameError(f"Wordlist with name {old_name} doesn't exist")
        if old_name != wordlist.name and wordlist.name in self.list_names():
            raise ConflictingEntryNameError(f"Wordlist with name {wordlist.name} already exists")
        self.__file_access.set_wordlist(wordlist.name, wordlist.entries)
        if old_name != wordlist.name:
            self.__file_access.delete_wordlist(old_name)
        self.__cache.update(old_name, wordlist)

    def delete(self, name: str):
        self.__cache.remove(name)
        self.__file_access.delete_wordlist(name)

    def list_names(self):
        return self.__file_access.list_wordlists()
