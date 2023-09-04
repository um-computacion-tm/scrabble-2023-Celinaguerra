import unittest
from game.scrabble import Tile
from game.scrabble import Cell


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value,5)

if __name__ == '__main__':
    unittest.main()