import random


class Player:
    def __init__(self, id:int, name=None):
        self.id = id
        bag = BagTiles()
        self.tiles = bag.take(7)
        self.score = 0
        
    def set_name(self, name):
        self.name = name
        return name

    #conectar con calculate_word_value
    """def score(self):
        self.score = score
""" 

class Dictionary:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)

    def load_words(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file)

    def valid_word(self, word):
        if word in self.words:
            return True
        else:
            return False

class Tile:
    def __init__(self,letter,value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('L',1),
            Tile('L',1),
            Tile('L',1),
            Tile('L',1),
            Tile('N',1),
            Tile('N',1),
            Tile('N',1),
            Tile('N',1),
            Tile('N',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('R',1),
            Tile('R',1),
            Tile('R',1),
            Tile('R',1),
            Tile('R',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('T',1),
            Tile('T',1),
            Tile('T',1),
            Tile('T',1),
            Tile('U',1),
            Tile('U',1),
            Tile('U',1),
            Tile('U',1),
            Tile('U',1),
            Tile('D',2),
            Tile('D',2),
            Tile('D',2),
            Tile('D',2),
            Tile('D',2),
            Tile('G',2),
            Tile('G',2),
            Tile('B',3),
            Tile('B',3),
            Tile('C',3),
            Tile('C',3),
            Tile('C',3),
            Tile('C',3),
            Tile('M',3),
            Tile('M',3),
            Tile('P',3),
            Tile('P',3),
            Tile('F',4),
            Tile('H',4),
            Tile('H',4),
            Tile('V',4),
            Tile('Y',4),
            Tile('Ch',5),
            Tile('Q',5),
            Tile('J',8),
            Tile('LL',8),
            Tile('Ñ',8),
            Tile('RR',8),
            Tile('X',8),
            Tile('Z',10),
            Tile('#',0),
            Tile('#',0),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self,tiles):
        self.tiles.extend(tiles)

class Cell:
    def __init__(self, multiplier=1, multiplier_type='', letter=None, word=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.word = word
        self.active = True 

    def add_letter(self, letter:Tile):
        self.letter = letter
    
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            value = self.letter.value * self.multiplier
            self.multiplier_type = None
            return value
        else:
            return self.letter.value
    
    def calculate_word_value(self,word):
        word_value = 0
        word_multiplier = 1
        for letter in word:
            word_value += letter.calculate_value()
            if letter.multiplier_type == 'word':
                word_multiplier = letter.multiplier
                letter.multiplier_type = None
        word_value *= word_multiplier
        return word_value

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1,'letter') for _ in range (15) ]
            for _ in range (15)
        ]

    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        pos_x = location[0]
        pos_y = location[1]

        if orientation == 'H':
            if pos_x + len_word > 15:
                return False
            else:
                return True
        elif orientation == 'V':
            if pos_y + len_word > 15:
                return False
            else:
                return True

    def is_empty(self):
        pass

class ScrabbleGame:
    def __init__(self, players_count:int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(id=_))
        self.current_player = None
        
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]

        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''

    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''