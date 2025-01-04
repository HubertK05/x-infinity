from wordlist import Wordlist
from wordlist_cache import WordlistCache
from wordlist_file_access import WordlistFileAccess


class WordlistDatabase:
    def __init__(self):
        self.__file_access = WordlistFileAccess()
        self.__cache = WordlistCache()

    def create(self, name: str):
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
        self.__file_access.set_wordlist(wordlist.name, wordlist.entries)
        self.__file_access.delete_wordlist(old_name)
        self.__cache.update(old_name, wordlist)

    def delete(self, name: str):
        self.__cache.remove(name)
        self.__file_access.delete_wordlist(name)

    def list_names(self):
        return self.__file_access.list_wordlists()
