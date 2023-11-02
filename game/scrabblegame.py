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

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.cell.calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def show_score(self):
        player_scores = {}
        for player in self.players:
            player_scores[player.get_name()] = player.get_score()
        return player_scores

    def play_turn(self):
        #jugador tiene x letras
        #da una palabra
        #verificar si se puede formar con las letras
        #verificar si existe
        #si es el primer turno -> que esté en el (7,7)
        #verificar si entra en el tablero
        #quitar letras (ver si se rellena la mano despues ahora o en el prox turno)
        #dar puntaje (chequear palabras alrededor)
        #pasar turno
        pass


    def playing(self):
        self.current_status = 'playing'

    def stopped_playing(self):
        self.current_status = 'not playing'

    # def validate_word_dictionary(self, word, location, orientation):
    #     if not self.dic.valid_word(word):
    #         raise InvalidWordException("Su palabra no existe en el diccionario")
    #     if not self.board.validate_word_inside_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra excede el tablero")
    #     if not self.board.validate_word_place_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")

    #quizás lo borro, ya existe algo similar en DIctionary