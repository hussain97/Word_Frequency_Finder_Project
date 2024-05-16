import unittest # Imports Python's built-in unit testing framework.
from unittest.mock import mock_open, patch # Allows you to mock file operations and other objects.
from word_frequency import read_file_content, count_word_frequencies, print_histogram # Import the created functions from the word_frequency file
from io import StringIO # Imports StringIO to capture output printed to stdout.
import sys # allows manipulating the Python runtime environment, including stdout.

class TestWordFrequencyFunctions(unittest.TestCase):  # Defines a test case class
    def test_read_file_content(self):  # Tests that read_file_content correctly reads the content of a file. # self allows for isolated and independent tests.
        mock_content = "apple banana apple"
        with patch("builtins.open", mock_open(read_data=mock_content)) as mocked_file: # 'patch' to mock the built-in open function, simulating the file reading process without needing an actual file.
            result = read_file_content("dummy_filename.txt")
            self.assertEqual(result, mock_content)
            print(result)
            print(mock_content)

    def test_read_file_non_existent(self): # Tests when attempting to read a non-existent file.
        with self.assertRaises(FileNotFoundError):
            read_file_content("non_existent_file.txt")

    def test_count_word_frequencies_empty_string(self): # Tests passing an empty string
        self.assertEqual(count_word_frequencies(""), {})

    def test_count_word_frequencies_single_word(self): # Tests a single word
        self.assertEqual(count_word_frequencies("apple"), {"apple": 1})

    def test_count_word_frequencies_multiple_occurrences(self): # Tests multople occurrences
        self.assertEqual(count_word_frequencies("apple banana apple"), {"apple": 2, "banana": 1})

    def test_count_word_frequencies_case_insensitive(self): # Tests case sensitivitiy
        self.assertEqual(count_word_frequencies("Apple apple"), {"Apple": 1, "apple": 1})

    def test_count_word_frequencies_with_punctuation(self): # Tests with punctuation
        self.assertEqual(count_word_frequencies("apple, apple! banana?"), {"apple,": 1, "apple!": 1, "banana?": 1})
        
    def test_count_word_frequencies_with_non_english_characters(self): # Tests with non english characters
        self.assertEqual(count_word_frequencies("تفاح Leggère 香蕉"), {"تفاح": 1, "Leggère": 1, "香蕉": 1})

    def test_print_histogram(self): # Tests if the printing of histogram is correct
        word_frequencies = {'apple': 2, 'banana': 1}
        expected_output = "apple: **\nbanana: *\n"
        captured_output = StringIO() # This object will be used to capture the output from the print_histogram function, which normally prints to the console.
        sys.stdout = captured_output # Any print statements executed after this line will write their output to captured_output instead of the console
        print_histogram(word_frequencies)
        sys.stdout = sys.__stdout__ # Revert to print to the console again
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
