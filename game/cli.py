from game.scrabblegame import *
from game.scrabble import *
from game.board import *
from game.player import *
from game.dictionary import *

def show_board(board):
    board = Board()
    print(board.set_board())

def main():
    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    game.playing()

    while game.current_status == 'playing':
        game.show_board()
        current_player = game.current_player
        print(f"Current Player: {current_player.get_name()}")
        try:
            game.play_turn()
        except Exception as e:
            print(e)
        if not game.bag_tiles.tiles:
            break
        
        action = input("Select an action:\n1) See your score\n2) See your tiles\n3) Stop the game\nChoice: ").strip()
        if action == '1':
            print(f"Your score: {current_player.get_score()} points")
        elif action == '2':
            print(f"Your tiles: {', '.join(tile.letter for tile in current_player.show_tiles())}")
        elif action == '3':
            stop_game = input("Do you want to stop the game (Y/N)? ").strip().lower()
            if stop_game == 'y':
                break
    scores = game.show_score()
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]
    if len(winners) == 1:
        print(f"Player {winners[0]} wins with {max_score} points!")
    else:
        print("It's a tie! The following players share the highest score:")
        for winner in winners:
            print(f"Player {winner}: {max_score} points")

def get_player_count():
    while True:
        try:
            player_count = int(input('cantidad de jugadores (1-3): '))
            if player_count <= 3:
                break
        except Exception as e:
            print('ingrese un numero válido por favor')
    return player_count


if __name__ == '__main__':
    main()