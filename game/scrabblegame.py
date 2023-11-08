from game.dictionary import Dictionary
from game.scrabble import BagTiles, Cell
from game.board import Board
from game.player import Player

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.dic = Dictionary(file_path="game/list_of_words.txt")
        self.cell = Cell()
        self.players = [Player() for _ in range(players_count)]
        self.current_player = None
        self.current_status = None

    def show_board(self):
        self.board.set_board()

    def next_turn(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        elif self.current_player == self.players[1]:
            self.current_player = self.players[0]
        elif self.current_player == None:
            self.current_player = self.players[0]

    def show_score(self):
        player_scores = {player: player.get_score() for player in self.players}
        return player_scores

    def validate_first_turn(self, word, location, orientation):
        self.board.validate_word_place_board(word, location, orientation)

    def validate_turn(self, word, location,orientation):
        self.board.validate_word_inside_board(word, location, orientation)