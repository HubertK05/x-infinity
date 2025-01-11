import pytest
from entry import Entry
from util import ConflictingEntryNameError, EmptyWordlistNameError
from wordlist import Wordlist


def test_wordlist_init():
    first_entry = Entry("word1", "meaning1")
    second_entry = Entry("word2", "meaning2")
    wordlist = Wordlist("test", [first_entry, second_entry])
    assert wordlist.name == "test"
    assert wordlist.get("word1") == first_entry
    assert wordlist.get("word2") == second_entry
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


def test_wordlist_adds_entry_correctly():
    wordlist = Wordlist("test", [])
    entry = Entry("word1", "meaning1")
    assert wordlist.get("word1") is None
    wordlist.add(entry)
    assert wordlist.get("word1") == entry
    assert wordlist.entries == [entry]


def test_wordlist_fails_to_add_duplicate_word_entry():
    wordlist = Wordlist("test", [])
    entry = Entry("word1", "meaning1")
    other_entry = Entry("word1", "meaning2")
    wordlist.add(entry)
    with pytest.raises(ConflictingEntryNameError):
        wordlist.add(other_entry)


def test_wordlist_removes_entry_correctly():
    entry = Entry("word1", "meaning1")
    wordlist = Wordlist("test", [entry])
    assert wordlist.get("word1") == entry
    wordlist.remove("word1")
    assert wordlist.get("word1") is None


def test_wordlist_updates_entry_correctly():
    entry = Entry("word1", "meaning1")
    wordlist = Wordlist("test", [entry])
    assert wordlist.get("word1") == entry
    updated_entry = Entry("word1", "meaning2")
    wordlist.update(updated_entry)
    assert wordlist.get("word1") == updated_entry


def test_wordlist_update_entry_with_nonexistent_name_fails():
    entry = Entry("word1", "meaning1")
    nonexistent_entry = Entry("word2", "meaning2")
    wordlist = Wordlist("test", [entry])
    with pytest.raises(ConflictingEntryNameError):
        wordlist.update(nonexistent_entry)
