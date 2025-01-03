import pytest
from entry import Entry
from util import EmptyWordlistNameError
from wordlist import Wordlist


def test_wordlist_init():
    first_entry = Entry("word1", "meaning1")
    second_entry = Entry("word2", "meaning2")
    wordlist = Wordlist("test", [first_entry, second_entry])
    assert wordlist.name == "test"
    assert wordlist.get("word1") == Entry("word1", "meaning1")
    assert wordlist.get("word2") == Entry("word2", "meaning2")
    assert wordlist.get("word3") is None


def test_wordlist_init_fails_with_empty_name():
    with pytest.raises(EmptyWordlistNameError):
        Wordlist("", [])


def test_wordlist_returns_entries_as_list_correctly():
    first_entry = Entry("word1", "meaning1")
    second_entry = Entry("word2", "meaning2")
    wordlist = Wordlist("test", [first_entry, second_entry])
    entries = sorted(wordlist.entries, key=lambda entry: entry.word)
    assert entries == [first_entry, second_entry]
