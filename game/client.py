from game.scrabble import ScrabbleGame

class Main:
    # def main():
    #     player_count = int(input('cantidad de jugadores'))
    #     game = ScrabbleGame(player_count)
    #     while(game.playing()):
    #         game...

    def main():
        player_count = get_player_count()
        game = ScrabbleGame(player_count)
        while game.is_playing():
            show_board(game.get_board())
            show_player(*game.get_current_player())
            word, coords, orientation = get_inputs()
            try:
                game.play(word, coords, orientation)
            except Exception as e:
                print(e)

    def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')
        return player_count