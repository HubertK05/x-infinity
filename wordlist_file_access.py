import json
from typing import Dict, List

from entry import Entry
import os

from util import InvalidWordlistNameError


class WordlistFileAccess:
    def __validate_wordlist_name(self, name: str):
        if any([char in name for char in ['/', '\\', '.']]):
            raise InvalidWordlistNameError("Wordlist cannot contain '/', '\\' or '.'")

    def get_wordlist(self, name: str) -> List[Entry]:
        self.__validate_wordlist_name(name)

        with open(f'data/{name}.json') as file:
            raw_data = file.read()
            if not raw_data:
                data = []
            else:
                data = json.loads(raw_data)
        return [Entry(entry['word'], entry['definition']) for entry in data]

    def set_wordlist(self, name: str, wordlist: List[Entry]):
        self.__validate_wordlist_name(name)
        entries = [entry.as_json() for entry in wordlist]

        with open(f'data/{name}.json', 'w') as file:
            file.write(json.dumps(entries, indent=4))

    def delete_wordlist(self, name: str):
        self.__validate_wordlist_name(name)

        os.remove(f'data/{name}.json')

    def list_wordlists(self) -> List[str]:
        return [file.split('.')[0] for file in os.listdir('data') if file.endswith('.json')]

    def get_full_data(self) -> List[Entry]:
        with open("full_data.json") as file:
            entries: List[Dict[str, str]] = json.load(file)
        return [Entry(entry["word"], entry["definition"]) for entry in entries]
