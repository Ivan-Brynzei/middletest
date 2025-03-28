import pytest
import os
from main import read_text_file, word_frequency, top_frequent_words, save_results, process_file

@pytest.fixture
def temp_input_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    content = """
    Hello, world! How is the world of programming?
    The world is big, and programming is exciting.
    Hello to everyone who loves coding.
    """
    file_path.write_text(content, encoding='utf-8')
    return str(file_path)

@pytest.fixture
def temp_output_file(tmp_path):
    return str(tmp_path / "test_output.txt")

def test_read_text_file(temp_input_file):
    content = read_text_file(temp_input_file)
    assert content.strip() == """
    Hello, world! How is the world of programming?
    The world is big, and programming is exciting.
    Hello to everyone who loves coding.
    """.strip()
    assert isinstance(content, str)

def test_read_text_file_not_found():
    content = read_text_file("non_existent_file.txt")
    assert content == ""

@pytest.mark.parametrize("text, expected", [
    ("hello hello world", {"hello": 2, "world": 1}),
    ("world, world. world!", {"world": 3}),
    ("", {}),
    ("python python PYTHON", {"python": 3}),
])
def test_word_frequency(text, expected):
    result = word_frequency(text)
    assert result == expected

@pytest.mark.parametrize("word_freq, top_n, expected", [
    ({"hello": 2, "world": 3, "code": 1}, 2, [("world", 3), ("hello", 2)]),
    ({"a": 1, "b": 2, "c": 3}, 1, [("c", 3)]),
    ({}, 5, []),
    ({"test": 5}, 10, [("test", 5)]),
])
def test_top_frequent_words(word_freq, top_n, expected):
    result = top_frequent_words(word_freq, top_n)
    assert result == expected

def test_save_results(temp_output_file):
    top_words = [("world", 3), ("hello", 2)]
    save_results(top_words, temp_output_file)
    
    with open(temp_output_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    assert content == "world-3\nhello-2"

def test_process_file_integration(temp_input_file, temp_output_file):
    process_file(temp_input_file, temp_output_file)
    
    with open(temp_output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) <= 10  
    assert all(line.strip().split('-')[1].isdigit() for line in lines)
