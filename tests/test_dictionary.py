import unittest
from game.scrabble import Dictionary
class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary('list_words.txt')

    def test_word_valid(self):
        result = self.dictionary.is_word_in_dic("casa")
        self.assertTrue(result)