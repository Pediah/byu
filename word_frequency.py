import os
import pandas as pd

def read_file(file_name):
    """
    Reads the content of the specified file and returns it as a string.

    Args:
    file_name (str): The name of the file to be read.

    Returns:
    str: The content of the file as a string.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."

def count_words(file_content):
    """
    Counts the frequency of each word in the given text content.

    Args:
    file_content (str): The text content to be analyzed.

    Returns:
    dict: A dictionary where keys are words and values are their frequencies.
    """
    word_freq = {}
    words = file_content.lower().split()
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def search_word_frequency(file_content, word):
    """
    Displays the frequency of a specific word in the given text content.

    Args:
    file_content (str): The text content to be analyzed.
    word (str): The word to search for.

    Returns:
    int: The frequency of the word in the text content.
    """
    word_freq = count_words(file_content)
    return word_freq.get(word.lower(), 0)

def test_read_file():
    # Test case 1: Test reading an existing file
    file_content = read_file("sample.txt")
    assert file_content == "This is a sample text file for testing purposes."

    # Test case 2: Test reading a non-existent file
    file_content = read_file("nonexistent.txt")
    assert file_content == "File not found."

def test_count_words():
    # Test case 1: Test counting words in a simple text
    text = "This is a simple text. It contains some words. It is simple."
    word_freq = count_words(text)
    assert word_freq == {'this': 2, 'is': 2, 'a': 1, 'simple': 2, 'text.': 1, 'it': 2, 'contains': 1, 'some': 1, 'words.': 1}

    # Test case 2: Test counting words in an empty text
    text = ""
    word_freq = count_words(text)
    assert word_freq == {}

def test_search_word_frequency():
    # Test case 1: Test searching for a word in the text
    text = "This is a sample text file for testing purposes."
    word = "sample"
    frequency = search_word_frequency(text, word)
    assert frequency == 1

    # Test case 2: Test searching for a word not in the text
    text = "This is a sample text file for testing purposes."
    word = "notfound"
    frequency = search_word_frequency(text, word)
    assert frequency == 0

if __name__ == "__main__":
    test_read_file()
    test_count_words()
    test_search_word_frequency()
    print("All tests passed successfully!")
