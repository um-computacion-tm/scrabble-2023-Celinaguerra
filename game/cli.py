from game.scrabblegame import ScrabbleGame
from game.scrabble import Board, Cell

    # def main():
    #     player_count = int(input('cantidad de jugadores'))
    #     game = ScrabbleGame(player_count)
    #     while(game.playing()):
    #         game...

    # def main():
    #     player_count = get_player_count()
    #     game = ScrabbleGame(player_count)
    #     while game.is_playing():
    #         show_board(game.get_board())
    #         show_player(*game.get_current_player())
    #         word, coords, orientation = get_inputs()
    #         try:
    #             game.play(word, coords, orientation)
    #         except Exception as e:
    #             print(e)

def get_player_count():
    while True:
        try:
            player_count = int(input('cantidad de jugadores (1-3): '))
            if player_count <= 3:
                break
        except Exception as e:
            print('ingrese un numero válido por favor')
    return player_count

def print_board(self):
    self.grid = [
            [Cell(1,'letter') for _ in range (15) ]
            for _ in range (15)
        ]
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
    second_part_print(self)
    # for i in range(10,15):
    #     row = self.grid[i]
    #     row_str = str(i) + " | "
    #     for cell in row:
    #         if cell.letter is None:
    #             row_str += ".  | "
    #         else:
    #             row_str += cell.letter + "  | "
    #     board += "\n" + row_str
    board += "\n"
    print(board)

def second_part_print(self):
    board = ''
    for i in range(10,15):
        row = self.grid[i]
        row_str = str(i) + " | "
        for cell in row:
            if cell.letter is None:
                row_str += ".  | "
            else:
                row_str += cell.letter + "  | "
        board += "\n" + row_str