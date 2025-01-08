import pytest
from letter import Letter
from util import InvalidLetterError


def test_letter_init():
    letter = Letter("a", False)
    assert letter.letter == "a"
    assert not letter.fixed


def test_letter_init_fails_with_empty_letter():
    with pytest.raises(InvalidLetterError):
        Letter("", False)


def test_letter_init_fails_with_invalid_length():
    with pytest.raises(InvalidLetterError):
        Letter("aa", False)
