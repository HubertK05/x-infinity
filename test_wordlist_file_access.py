import pytest
from wordlist_file_access import WordlistFileAccess
from util import InvalidWordlistNameError


def test_wordlist_database_get_invalid_wordlist_name():
    db = WordlistFileAccess()
    with pytest.raises(InvalidWordlistNameError):
        db.get_wordlist("/")


def test_wordlist_database_set_invalid_wordlist_name():
    db = WordlistFileAccess()
    with pytest.raises(InvalidWordlistNameError):
        db.set_wordlist("/", [])


def test_wordlist_database_delete_invalid_wordlist_name():
    db = WordlistFileAccess()
    with pytest.raises(InvalidWordlistNameError):
        db.delete_wordlist("/")
