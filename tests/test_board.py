import unittest
from game.scrabble import Board, Tile

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

    def test_word_outside_board_x(self):
        board = Board()
        word = 'jalapeño'
        location = (10,10)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        assert word_is_valid == False

    def test_word_outside_board_y(self):
        board = Board()
        word = 'mantis'
        location = (1,14)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        assert word_is_valid == False

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        actually_empty = board.validate_empty()
        assert actually_empty == False

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        #word_is_valid = board.validate_word_place_board(word, location, orientation)
        word_is_valid = board.put_words(word, location, orientation) #es put lo mismo que validate?
        assert word_is_valid == True

if __name__ == "__main__":
    unittest.main