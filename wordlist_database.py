import json
from typing import List

from entry import Entry
import os

from util import InvalidWordlistNameError


def validate_wordlist_name(name: str):
    if any([char in name for char in ['/', '\\', '.']]):
        raise InvalidWordlistNameError("Wordlist cannot contain '/', '\\' or '.'")


class WordlistDatabase:
    def __init__(self):
        pass

    def get_wordlist(self, name: str) -> List[Entry]:
        validate_wordlist_name(name)

        with open(f'{name}.json') as file:
            data = json.loads(file.read())
        return [Entry(entry['word'], entry['definition']) for entry in data]

    def set_wordlist(self, name: str, wordlist: List[Entry]):
        validate_wordlist_name(name)

        with open(f'{name}.json', 'w') as file:
            file.write(json.dumps(wordlist, indent=4))

    def delete_wordlist(self, name: str):
        validate_wordlist_name(name)

        os.remove(f'{name}.json')
