import pytest
from entry import Entry
from util import ConflictingEntryNameError
from wordlist import Wordlist
from wordlist_cache import WordlistCache


def test_wordlist_cache_init():
    cache = WordlistCache()
    assert cache.wordlists == []


def test_wordlist_cache_add_wordlist():
    cache = WordlistCache()
    wordlist = Wordlist("test", [])
    cache.add(wordlist)
    assert cache.wordlists == [wordlist]


def test_wordlist_cache_add_wordlist_duplicate_name_fails():
    cache = WordlistCache()
    wordlist = Wordlist("test", [])
    other_wordlist = Wordlist("test", [Entry("word", "definition")])
    cache.add(wordlist)
    with pytest.raises(ConflictingEntryNameError):
        cache.add(other_wordlist)


def test_wordlist_cache_get_word():
    cache = WordlistCache()
    wordlist = Wordlist("test", [])
    cache.add(wordlist)
    assert cache.get("test") == wordlist


def test_wordlist_cache_get_nonexistent_word_returns_none():
    cache = WordlistCache()
    assert cache.get("test") is None


def test_wordlist_cache_update_wordlist_name():
    cache = WordlistCache()
    wordlist = Wordlist("test", [])
    updated_wordlist = Wordlist("new name", [])
    cache.add(wordlist)
    assert cache.wordlists == [wordlist]
    cache.update("test", "new name")
    assert cache.wordlists == [updated_wordlist]


def test_wordlist_cache_update_nonexistent_wordlist_name_fails():
    cache = WordlistCache()
    with pytest.raises(ConflictingEntryNameError):
        cache.update("test", "new name")


def test_wordlist_cache_update_wordlist_to_duplicate_name_fails():
    cache = WordlistCache()
    first = Wordlist("test1", [])
    second = Wordlist("test2", [])
    cache.add(first)
    cache.add(second)
    with pytest.raises(ConflictingEntryNameError):
        cache.update("test1", "test2")


def test_wordlist_cache_remove_wordlist():
    cache = WordlistCache()
    wordlist = Wordlist("test", [])
    cache.add(wordlist)
    assert cache.wordlists == [wordlist]
    cache.remove("test")
    assert cache.wordlists == []


def test_wordlist_cache_remove_nonexistent_wordlist_does_nothing():
    cache = WordlistCache()
    assert cache.wordlists == []
    cache.remove("test")
    assert cache.wordlists == []
