import unittest
from word_frequency_counter import read_file, count_words, search_word_frequency

class TestWordFrequency(unittest.TestCase):
    def test_read_file_existing(self):
        file_content = read_file("sample.txt")
        self.assertEqual(file_content, "This is a sample text file for testing purposes.")

    def test_read_file_nonexistent(self):
        file_content = read_file("nonexistent.txt")
        self.assertEqual(file_content, "File not found.")

    def test_count_words_simple_text(self):
        text = "This is a simple text. It contains some words. It is simple."
        word_freq = count_words(text)
        self.assertEqual(word_freq, {'this': 2, 'is': 2, 'a': 1, 'simple': 2, 'text.': 1, 'it': 2, 'contains': 1, 'some': 1, 'words.': 1})

    def test_count_words_empty_text(self):
        text = ""
        word_freq = count_words(text)
        self.assertEqual(word_freq, {})

    def test_search_word_frequency_existing(self):
        text = "This is a sample text file for testing purposes."
        word = "sample"
        frequency = search_word_frequency(text, word)
        self.assertEqual(frequency, 1)

    def test_search_word_frequency_nonexisting(self):
        text = "This is a sample text file for testing purposes."
        word = "notfound"
        frequency = search_word_frequency(text, word)
        self.assertEqual(frequency, 0)

if __name__ == '__main__':
    unittest.main()
