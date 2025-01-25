import pytest
from text_tool import count_words, longest_word

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("") == 0

def test_longest_word():
    assert longest_word("Hello world") == "Hello"
    assert longest_word("") is None
