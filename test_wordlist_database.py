import pytest
from wordlist_database import WordlistDatabase
from util import InvalidWordlistNameError


def test_wordlist_database_get_invalid_wordlist_name():
    db = WordlistDatabase()
    with pytest.raises(InvalidWordlistNameError):
        db.get_wordlist("/")


def test_wordlist_database_set_invalid_wordlist_name():
    db = WordlistDatabase()
    with pytest.raises(InvalidWordlistNameError):
        db.set_wordlist("/", [])


def test_wordlist_database_delete_invalid_wordlist_name():
    db = WordlistDatabase()
    with pytest.raises(InvalidWordlistNameError):
        db.delete_wordlist("/")
