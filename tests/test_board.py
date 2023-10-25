import unittest
from game.scrabble import Tile
from game.board import Board, TW, TL, DW, DL, OutOfBoard

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
        word = 'FACULTAD'
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
        try:
            board.validate_word_inside_board(word,location,orientation)
            assert False
        except OutOfBoard as e:
            assert str(e)

    def test_word_outside_board_y(self):
        board = Board()
        word = 'mantis'
        location = (1,14)
        orientation = 'V'
        try:
            board.validate_word_inside_board(word,location,orientation)
            assert False
        except OutOfBoard as e:
            assert str(e)

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        actually_empty = board.validate_empty()
        assert actually_empty == False


    def test_put_words_horizontal(self):
        board = Board()
        board.put_words("HOLA", (5, 5), "H")
        # ver si la palabra esta donde tiene que estar
        for i in range(5, 9):
            self.assertEqual(board.grid[5][i].letter, "HOLA"[i - 5])

    def test_put_words_vertical_and_print(self):
        board = Board()
        board.put_words("LAPIZ", (4, 4), "V")
        for i in range(4, 8):
            self.assertEqual(board.grid[i][4].letter, "LAPIZ"[i - 4])

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (5, 7) #Originalmente decía (7,4), pero entonces no pasaba por el centro y assert era equivocado
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 6) #Idem test_place_word_empty_horizontal_fine
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1))
        word = "FACULTAD"
        location = (4, 7)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_multipliers_placement(self):
        board = Board()

        for location in TW:
            cell = board.grid[location[0]][location[1]]
            self.assertEqual(cell.multiplier_type, 'word')
            self.assertEqual(cell.multiplier, 3)

        for location in DW:
            cell = board.grid[location[0]][location[1]]
            self.assertEqual(cell.multiplier_type, 'word')
            self.assertEqual(cell.multiplier, 2)

        for location in TL:
            cell = board.grid[location[0]][location[1]]
            self.assertEqual(cell.multiplier_type, 'letter')
            self.assertEqual(cell.multiplier, 3)

        for location in DL:
            cell = board.grid[location[0]][location[1]]
            self.assertEqual(cell.multiplier_type, 'letter')
            self.assertEqual(cell.multiplier, 2)

if __name__ == "__main__":
    unittest.main