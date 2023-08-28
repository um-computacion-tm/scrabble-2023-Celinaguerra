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


if __name__ == "__main__":
    unittest.main