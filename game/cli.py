from game.scrabblegame import ScrabbleGame
from game.scrabble import Cell
from game.board import Board

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

def show_board(board):
    board = Board()
    print(board.set_board())