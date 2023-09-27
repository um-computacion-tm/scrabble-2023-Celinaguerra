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


    def test_put_words_horizontal(self):
        board = Board()
        board.put_words("hola", (5, 5), "H")
        # ver si la palabra esta donde tiene que estar
        for i in range(5, 9):
            self.assertEqual(board.grid[5][i].letter, "hola"[i - 5])

    def test_put_words_vertical_and_print(self):
        board = Board()
        board.put_words("lapiz", (4, 4), "V")
        # ver si la palabra esta donde tiene que estar
        for i in range(4, 8):
            self.assertEqual(board.grid[i][4].letter, "lapiz"[i - 4])
        board.print_board()

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
        word = "Facultad"
        location = (8, 6)
        orientation = "V" # ORIGINALMENTE dceía H pero si no no pasaba por la otra palabra
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

if __name__ == "__main__":
    unittest.main