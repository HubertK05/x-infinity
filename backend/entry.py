from backend.util import EmptyEntryError


class Entry:
    """A single word - definition combination."""

    def __init__(self, word: str, definition: str):
        """
        Initializes an entry, consisting of non-empty `word` and `definition`.
        Note that the definition can be empty.

        ## Throws:
        - `EmptyEntryError` - if `word` is empty.
        """
        if not word:
            raise EmptyEntryError("Word is empty")
        self.word = word
        self.definition = definition

    def as_json(self):
        """Returns the dictionary of properties."""
        return {"word": self.word, "definition": self.definition}
