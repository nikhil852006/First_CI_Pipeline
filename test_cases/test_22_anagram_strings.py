import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_valid_anagrams():
    assert is_anagram("listen", "silent") is True


def test_different_strings():
    assert is_anagram("hello", "world") is False


def test_uppercase_letters():
    assert is_anagram("Listen", "Silent") is True


def test_spaces():
    assert is_anagram("dormitory", "dirty room") is True


def test_same_string():
    assert is_anagram("python", "python") is True
