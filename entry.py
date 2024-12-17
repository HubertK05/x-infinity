from util import EmptyEntryError


class Entry:
    def __init__(self, word: str, definition: str):
        if not word:
            raise EmptyEntryError("Word is empty")
        if not definition:
            raise EmptyEntryError("Definition is empty")
        self.word = word
        self.definition = definition
