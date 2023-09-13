import unittest
from game.scrabble import Dictionary

class TestDictionary(unittest.TestCase):
    def test_word_in_dictionary(self):
        dictionary = Dictionary("game/list_of_words.txt")
        self.assertEqual(dictionary.valid_word('sueño'), True)
    
    def test_word_not_dictionary(self):
        dictionary = Dictionary("game/list_of_words.txt")
        self.assertEqual(dictionary.valid_word('kjashdkja'), False) 

if __name__ == "__main__":
    unittest.main