from crossword import Crossword
from entry import Entry


def test_crossword_init():
    entry = Entry("word", "definition")
    crossword = Crossword(0, [(1, entry)])
    assert crossword.solution_column == 0
    assert crossword.entries == [(1, entry)]
