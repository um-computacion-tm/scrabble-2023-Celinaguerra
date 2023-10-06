import unittest
from game.scrabble import Dictionary

class TestDictionary(unittest.TestCase):
    def test_word_in_dictionary(self):
        dictionary = Dictionary("game/list_of_words.txt")
        self.assertEqual(dictionary.valid_word('SUEÑO'), True)
    
    def test_word_not_dictionary(self):
        dictionary = Dictionary("game/list_of_words.txt")
        self.assertEqual(dictionary.valid_word('KAJSDKSA'), False) 

    def test_word_not_dictionary_but_letter_is(self):
        dictionary = Dictionary("game/list_of_words.txt")
        self.assertEqual(dictionary.valid_word('AA'), False) 

if __name__ == "__main__":
    unittest.main