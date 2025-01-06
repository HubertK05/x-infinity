import pytest
from crossword import Crossword
from entry import Entry
from util import InvalidCrosswordError


def test_crossword_init():
    entry = Entry("word", "definition")
    crossword = Crossword(0, [(1, entry)])
    assert crossword.solution_column == 0
    assert crossword.entries == [(1, entry)]


def test_crossword_init_fails_if_empty():
    with pytest.raises(InvalidCrosswordError):
        Crossword(1, [])


def test_crossword_init_fails_if_solution_column_negative():
    with pytest.raises(InvalidCrosswordError):
        Crossword(-1, [])


def test_crossword_init_fails_if_entry_column_negative():
    with pytest.raises(InvalidCrosswordError):
        Crossword(1, [(-1, Entry("word", "definition"))])


def test_crossword_width():
    crossword = Crossword(0, [(1, Entry("word", "definition"))])
    assert crossword.width() == 5


def test_crossword_width_multiple_entries():
    crossword = Crossword(0, [
        (0, Entry("word", "definition")),
        (5, Entry("w", "definition")),
        (2, Entry("word", "definition"))
    ])
    assert crossword.width() == 6
