import json
from typing import Dict, List

from entry import Entry
import os

from util import InvalidWordlistNameError
from wordlist import Wordlist


class WordlistFileAccess:
    """A class responsible for managing wordlists inside the filesystem."""

    def __validate_wordlist_name(self, name: str):
        """
        Checks if `name` is alphanumeric. This is for the safety reason - to
        prevent modifying unwanted directories.
        """
        if not name.isalnum():
            raise InvalidWordlistNameError("Wordlist name contains non-alphanumeric characters")

    def get_wordlist(self, name: str) -> Wordlist:
        """
        Fetches the wordlist from a file in the `data` directory.

        ## Parameters:
        - name - the filename to fetch data from.

        ## Throws:
        - `InvalidWordlistNameError` if name has non-alphanumeric characters.
        """
        self.__validate_wordlist_name(name)

        with open(f'data/{name}.json') as file:
            raw_data = file.read()
            if not raw_data:
                data = []
            else:
                data = json.loads(raw_data)
        return Wordlist(name, [Entry(entry['word'], entry['definition']) for entry in data])

    def set_wordlist(self, wordlist: Wordlist):
        """
        Inserts or updates `wordlist` to a file in the `data` directory.

        ## Parameters:
        - wordlist - the inserted wordlist. The filename is under the
        `wordlist.name`

        ## Throws:
        - `InvalidWordlistNameError` if name has non-alphanumeric characters.
        """
        self.__validate_wordlist_name(wordlist.name)
        entries = [entry.as_json() for entry in wordlist.entries]

        with open(f'data/{wordlist.name}.json', 'w') as file:
            file.write(json.dumps(entries, indent=4))

    def delete_wordlist(self, name: str):
        """
        Removes the wordlist file in the `data` directory.

        ## Parameters:
        - name - the name of the file to remove.

        ## Throws:
        - `InvalidWordlistNameError` if name has non-alphanumeric characters.
        """
        self.__validate_wordlist_name(name)
        os.remove(f'data/{name}.json')

    def rename_wordlist(self, old_name: str, name: str):
        """
        Renames the wordlist file at `old_name` to `name`.

        ## Parameters:
        - old_name - the name of the file to rename.
        - name - the new name.

        ## Throws:
        - `InvalidWordlistNameError` if either `old_name` or `name` have
        non-alphanumeric characters.
        """
        self.__validate_wordlist_name(name)
        self.__validate_wordlist_name(old_name)
        os.rename(f'data/{old_name}.json', f'data/{name}.json')

    def list_wordlists(self) -> List[str]:
        """
        Lists all wordlist file names of the `data` directory.
        """
        return [file.split('.')[0] for file in os.listdir('data') if file.endswith('.json')]

    def get_full_data(self) -> List[Entry]:
        """
        Returns data at `full_data.json`.
        """
        with open("full_data.json") as file:
            entries: List[Dict[str, str]] = json.load(file)
        return [Entry(entry["word"], entry["definition"]) for entry in entries]
