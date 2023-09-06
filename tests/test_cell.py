import unittest
from game.scrabble import Cell
from game.scrabble import Tile

class TestCell(unittest.TestCase):
    def test__init__(self):
        cell = Cell(multiplier = 2, multiplier_type = 'letter')
        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier = 1, multiplier_type = '')
        letter = Tile(letter = 'p', value = 3)
        cell.add_letter(letter = letter)
        self.assertEqual(
            cell.letter, letter
        )

    def test_cell_value(self):
        cell = Cell(multiplier = 2, multiplier_type = 'letter')
        letter = Tile(letter = 'p', value = 3)
        cell.add_letter(letter = letter)
        self.assertEqual(
            cell.calculate_value(), 
            6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier = 2, multiplier_type = 'word')
        letter = Tile(letter = 'p', value = 3)
        cell.add_letter(letter=letter)
        self.assertEqual(
            cell.calculate_value(),
            3,
        )

    def test_with_letter_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value,7)

    def test_with_word_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value,10)

    def test_with_letter_word_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1),
                ),
            Cell(letter=Tile('A', 1)),
            Cell(
                multiplier=2,
                multiplier_type='word',
                letter=Tile('S', 2)
                ),
            Cell(letter=Tile('A', 1)),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value,14)


if __name__ == "__main__":
    unittest.main


