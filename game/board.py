from game.scrabble import Cell
class OutOfBoard(Exception):
    pass

TW = ((0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14))
DW = ((1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13, 13), (12, 12), (11, 11), (10, 10))
TL = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9))
DL = ((0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))

class Board:
    def __init__(self):
        self.is_empty = True
        self.grid = [
            [Cell(1,'letter') for _ in range (15) ]
            for _ in range (15)
        ]
        self.cells_with_score_multiplier()

    def validate_empty(self):
        if self.grid[7][7] is not None:
            self.is_empty = False
        return self.is_empty


    def put_words(self, word, location, orientation):
        len_word = len(word)
        pos_x = location[1]
        pos_y = location[0]
        if orientation == 'H':
            for i in range (len_word):
                self.grid[pos_x][pos_y + i].add_letter(word[i])
        else:
            for i in range (len_word):
                self.grid[pos_x + i][pos_y].add_letter(word[i])

    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        pos_x = location[0]
        pos_y = location[1]

        if orientation == 'H':
            if pos_x + len_word > 15:
                raise OutOfBoard("The word you picked is outside the board")
            else:
                return True
        elif orientation == 'V':
            if pos_y + len_word > 15:
                raise OutOfBoard("The word you picked is outside the board")
            else:
                return True

    def validate_word_place_board(self,word,location,orientation):
        center_of_board = (7, 7)
        for i in range(len(word)):
            pos_x = location[0] + i if orientation == "H" else location[0] #si es h, va sumando i horizontalmente
            pos_y = location[1] + i if orientation == "V" else location[1] # idem vertical
            # print(f"posicion ({pos_x}, {pos_y}) de letra '{word[i]}'")
            if pos_x == center_of_board[0] and pos_y == center_of_board[1]: # si x e y son 7,7
                # print ("pasa por el centro")
                return True
        return False


    def cell_multiplier(self, location, multiplier_type, multiplier):
        pos_x = location[0]
        pos_y = location[1]
        cell = self.grid[pos_x][pos_y]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier

    def cells_with_score_multiplier(self):
        for location in TW:
            self.cell_multiplier(location, 'word', 3)
        for location in DW:
            self.cell_multiplier(location, 'word', 2)
        for location in TL:
            self.cell_multiplier(location, 'letter', 3)
        for location in DL:
            self.cell_multiplier(location, 'letter', 2)


    def set_board(self):
        board = ""
        board += "\n"
        #header row
        board += "   | " + "  | ".join(str(item) for item in range(0,10)) + "  | " + " | ".join(str(item) for item in range(10,15)) + " | "
        board += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        for i in range(0,15):
            row = self.grid[i]
            row_str = str(i) + "  | "
            for cell in row:
                if cell.letter is None:
                    row_str += ".  | "
                else:
                    row_str += cell.letter + "  | "
            board += "\n" + row_str
        board += "\n"
        print(board)