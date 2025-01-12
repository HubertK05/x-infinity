import pytest
from backend.entry import Entry
from backend.util import EmptyEntryError


def test_init_entry():
    entry = Entry("word", "definition")
    assert entry.word == "word"
    assert entry.definition == "definition"


def test_init_entry_empty_word_fails():
    with pytest.raises(EmptyEntryError):
        Entry("", "definition")


def test_init_entry_empty_definition_succeeds():
    entry = Entry("word", "")
    assert entry.definition == ""
