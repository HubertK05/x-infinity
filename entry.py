from util import EmptyEntryError


class Entry:
    def __init__(self, word: str, definition: str):
        if not word:
            raise EmptyEntryError("Word is empty")
        self.word = word
        self.definition = definition

    def as_json(self):
        return {"word": self.word, "definition": self.definition}
