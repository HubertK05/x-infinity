import pytest
from crossword import Crossword
from entry import Entry
from letter import Letter
from util import InvalidCrosswordError


def test_crossword_init():
    entry = Entry("word", "definition")
    crossword = Crossword(0, [(1, entry)])
    assert crossword.solution_column == 0
    assert crossword.entries == [(1, entry)]
    assert crossword.state == [(
        1,
        [
            Letter("", False),
            Letter("", False),
            Letter("", False),
            Letter("", False)
        ]
    )]


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


def test_crossword_get_letter():
    crossword = Crossword(0, [
        (0, Entry("word", "meaning")),
        (2, Entry("another", "meaning"))
        ])
    letter = crossword.get_letter(1, 3)
    assert letter == Letter("", False)


def test_crossword_set_letter():
    crossword = Crossword(0, [
        (0, Entry("word", "meaning")),
        (2, Entry("another", "meaning"))
        ])
    crossword.set_letter(0, 2, "x")
    result = crossword.get_letter(0, 2)
    assert result == Letter("x", False)


def test_crossword_set_fixed_letter_does_not_change_it():
    crossword = Crossword(0, [
        (0, Entry("word", "meaning")),
        (2, Entry("another", "meaning"))
        ])
    crossword.set_letter(0, 2, "r")
    assert crossword.get_letter(0, 2) == Letter("r", False)
    crossword.fix_letter(0, 2)
    assert crossword.get_letter(0, 2) == Letter("r", True)
    crossword.set_letter(0, 2, "")
    assert crossword.get_letter(0, 2) == Letter("r", True)


def test_crossword_fix_letter():
    crossword = Crossword(0, [(0, Entry("word", "meaning"))])
    assert crossword.get_letter(0, 2) == Letter("", False)
    crossword.fix_letter(0, 2)
    assert crossword.get_letter(0, 2) == Letter("r", True)


def test_crossword_check():
    crossword = Crossword(2, [(0, Entry("word", "test")), (2, Entry("another", "test"))])
    crossword.set_letter(0, 0, "w")
    crossword.set_letter(0, 1, "r")
    crossword.set_letter(1, 2, "o")
    crossword.set_letter(1, 3, "r")
    check_results = crossword.check()
    assert check_results == [
        (0, 0, True),
        (0, 1, False),
        (1, 4, True),
        (1, 5, False)
    ]
