from game.dictionary import Dictionary
from game.scrabble import BagTiles, Player, Board, Cell

class ScrabbleGame:
    def __init__(self, players_count:int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player())
        self.current_player = None
        self.dic = Dictionary(file_path="game/list_of_words.txt")
        self.cell = Cell()
        
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

    # def validate_word_dictionary(self, word, location, orientation):
    #     if not self.dic.valid_word(word):
    #         raise InvalidWordException("Su palabra no existe en el diccionario")
    #     if not self.board.validate_word_inside_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra excede el tablero")
    #     if not self.board.validate_word_place_board(word, location, orientation):
    #         raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")

    #quizás lo borro, ya existe algo similar en DIctionary