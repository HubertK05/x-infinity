import json
from typing import List

from entry import Entry
import os

from util import InvalidWordlistNameError


def validate_wordlist_name(name: str):
    if any([char in name for char in ['/', '\\', '.']]):
        raise InvalidWordlistNameError("Wordlist cannot contain '/', '\\' or '.'")


class WordlistFileAccess:
    def __init__(self):
        pass

    def get_wordlist(self, name: str) -> List[Entry]:
        validate_wordlist_name(name)

        with open(f'data/{name}.json') as file:
            raw_data = file.read()
            if not raw_data:
                data = []
            else:
                data = json.loads(raw_data)
        return [Entry(entry['word'], entry['definition']) for entry in data]

    def set_wordlist(self, name: str, wordlist: List[Entry]):
        validate_wordlist_name(name)

        with open(f'data/{name}.json', 'w') as file:
            file.write(json.dumps(as_json(wordlist), indent=4))

    def delete_wordlist(self, name: str):
        validate_wordlist_name(name)

        os.remove(f'data/{name}.json')

    def list_wordlists(self) -> List[str]:
        return [file.split('.')[0] for file in os.listdir('data') if file.endswith('.json')]


def as_json(entries: List[Entry]):
    return [{"word": entry.word, "definition": entry.definition} for entry in entries]
