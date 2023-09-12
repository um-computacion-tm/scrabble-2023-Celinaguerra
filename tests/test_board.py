import unittest
from game.scrabble import Board

class TestBoard(unittest.TestCase):
    def test__init__(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_word_inside_board_x(self):
        board = Board()
        word = 'facultad'
        location = (5,10)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True


    def test_word_inside_board_y(self):
        board = Board()
        word = 'dragon'
        location = (13,1)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True


if __name__ == "__main__":
    unittest.main