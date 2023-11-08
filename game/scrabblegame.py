from game.dictionary import Dictionary
from game.scrabble import BagTiles, Cell
from game.board import Board
from game.player import Player

class ScrabbleGame:
    def __init__(self, players_count:int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
        self.current_player = None
        self.dic = Dictionary(file_path="game/list_of_words.txt")
        self.cell = Cell()
        self.current_status = None
        
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]


    def show_score(self):
        player_scores = {}
        for player in self.players:
            player_scores[player.get_name()] = player.get_score()
        return player_scores

    # def play_turn(self):
    #     #jugador tiene x letras
    #     #da una palabra
    #     #verificar si se puede formar con las letras
    #     #verificar si existe
    #     #si es el primer turno -> que esté en el (7,7)
    #     #verificar si entra en el tablero
    #     #quitar letras (ver si se rellena la mano despues ahora o en el prox turno)
    #     #dar puntaje (chequear palabras alrededor)
    #     #pasar turno
    #     pass

    def play_turn(self):
        player = self.current_player
        player_tiles = player.show_tiles()
        self.show_board()
        print(f"Current player: {player.get_name()}")
        print(f"Your tiles: {', '.join(tile.letter for tile in player_tiles)}")

        word = input("Enter the word you want to play: ").upper()
        location = tuple(map(int, input("Enter the location (row, column): ").split(',')))
        orientation = input("Enter the orientation (H for horizontal, V for vertical): ").upper()

        try:
            if not player.has_letters(word):
                raise Exception("You don't have the required letters to form this word.")
            if not self.dic.valid_word(word):
                raise Exception("The word is not valid according to the dictionary.")

            if self.current_player == self.players[0] and self.validate_empty():
                if location != (7, 7):
                    raise Exception("In the first turn, the word must pass through the center (7, 7).")
                self.board.put_words(word, location, orientation)
            else:
                if not self.validate_word_inside_board(word, location, orientation):
                    raise Exception("Invalid word placement on the board.")
                if not self.validate_word_place_board(word, location, orientation):
                    raise Exception("The word is not properly placed on the board.")
                self.board.put_words(word, location, orientation)

            words = self.board.put_words(word, location, orientation)
            total = self.cell.calculate_word_value(words)
            player.increase_score(total)
            player.refill(self.bag_tiles)
            self.next_turn()

        except Exception as e:
            print(f"Error: {e}")


    def playing(self):
        self.current_status = 'playing'

    def stopped_playing(self):
        self.current_status = 'not playing'