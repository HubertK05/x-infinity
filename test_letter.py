import pytest
from letter import Letter
from util import InvalidLetterError


def test_letter_init():
    letter = Letter("a", False)
    assert letter.letter == "a"
    assert not letter.fixed


def test_letter_init_fails_with_empty_letter():
    letter = Letter("", False)
    assert letter.letter == ""
    assert not letter.fixed


def test_letter_init_fails_with_invalid_length():
    with pytest.raises(InvalidLetterError):
        Letter("aa", False)


def test_letter_mutation_fails_with_invalid_length():
    letter = Letter("a", False)
    with pytest.raises(InvalidLetterError):
        letter.letter = "aa"
