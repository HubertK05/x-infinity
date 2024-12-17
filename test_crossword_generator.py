from crossword import Crossword
from crossword_generator import CrosswordGenerator
from entry import Entry


def test_crossword_generator_init():
    generator = CrosswordGenerator()
    assert generator.entries == []


def test_crossword_generator_set_entries():
    generator = CrosswordGenerator()
    entry = Entry("word", "definition")
    generator.entries = [entry]
    assert generator.entries == [entry]


def test_generate_crossword():
    generator = CrosswordGenerator()
    the_entry = Entry("the", "the definition")
    cat_entry = Entry("cat", "cat definition")
    a_entry = Entry("a", "a definition"),
    entries = [the_entry, cat_entry, a_entry]
    generator.entries = entries
    result: Crossword = generator.generate("eat")

    # This is the only solution
    assert result.solution_column == 2
    assert result.entries == [
        (0, the_entry),
        (2, a_entry),
        (0, cat_entry),
    ]
