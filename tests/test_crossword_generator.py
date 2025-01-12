import pytest
from backend.crossword import Crossword
from backend.crossword_generator import CrosswordGenerator
from backend.entry import Entry
from backend.util import CrosswordGenerationError


def test_crossword_generator_init():
    generator = CrosswordGenerator()
    assert generator.entries == []


def test_crossword_generator_set_entries():
    generator = CrosswordGenerator()
    entry = Entry("word", "definition")
    generator.entries = [entry]
    assert generator.entries == [entry]


def noop(_collection):
    pass


def test_find_random_matching(monkeypatch):
    monkeypatch.setattr("random.shuffle", noop)

    generator = CrosswordGenerator()
    the_entry = Entry("the", "the definition")
    a_entry = Entry("a", "a definition")
    cat_entry = Entry("cat", "cat definition")
    entries = [the_entry, a_entry, cat_entry]
    generator.entries = entries

    result: list[tuple[int, Entry]] = generator._find_random_matching("eat")

    # This is the only solution
    assert result == [
        (2, the_entry),
        (0, a_entry),
        (2, cat_entry),
    ]


def test_generate_crossword_using_random_matching(monkeypatch):
    monkeypatch.setattr("random.shuffle", noop)

    generator = CrosswordGenerator()
    the_entry = Entry("the", "the definition")
    a_entry = Entry("a", "a definition")
    cat_entry = Entry("cat", "cat definition")
    entries = [the_entry, a_entry, cat_entry]
    generator.entries = entries

    result: Crossword = generator.generate("eat")

    # This is the only solution
    assert result.solution_column == 2
    assert result.solution == [
        (0, the_entry),
        (2, a_entry),
        (0, cat_entry),
    ]


def test_find_random_matching_fails_on_insufficient_words():
    generator = CrosswordGenerator()
    the_entry = Entry("the", "the definition")
    a_entry = Entry("a", "a definition")
    cat_entry = Entry("cat", "cat definition")
    entries = [the_entry, a_entry, cat_entry]
    generator.entries = entries

    # with pytest.raises(CrosswordGenerationError):
    assert generator._find_random_matching("aca") is None
