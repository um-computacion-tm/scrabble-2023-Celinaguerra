import random
from collections import Counter

class InvalidWordException:
    pass
class InvalidPlaceWordException:
    pass

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

    def add_letter(self, letter:Tile):
        self.letter = letter
    
    def calculate_letter_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
    
    def calculate_word_value(self,word):
        total_value = 0
        word_multiplier = 1
        
        # for letter in word:
        #     total_value += letter.calculate_letter_value()
        #     if letter.multiplier_type == 'word':
        #         word_multiplier = letter.multiplier
        #         letter.multiplier_type = None
        # total_value *= word_multiplier
        # return total_value

        for self in word:
            if self.multiplier_type == 'letter':
                total_value += self.calculate_letter_value()
            if self.multiplier_type == 'word':
                total_value += self.calculate_letter_value()
                word_multiplier *= self.multiplier
            else:
                total_value += self.letter.value
        total_value *= word_multiplier
        return total_value

class Player:
    def __init__(self):
        self.name = ""
        self.tiles = []
        self.score = 0

    def set_name(self,name):
        self.name = name
    
    def get_name(self):
        return self.name

    def take_tiles(self, bag:BagTiles, amount):
        self.tiles.extend(bag.take(amount))
    
    def increase_score(self,amount):
        self.score += amount

    def get_score(self):
        return self.score

    def refill(self,bag:BagTiles):
        self.tiles += bag.take(
            7- len(self.tiles)
        )

    def has_letters(self, tiles=[]):
        letras_jugador = [tile.letter for tile in self.tiles]
        letras_palabra = [tile.letter for tile in tiles]
        letras_necesarias = Counter(letras_palabra)
        for letra, cantidad in letras_necesarias.items():
            if letras_jugador.count(letra) < cantidad:
                return False
        return True


class Board:
    def __init__(self):
        self.is_empty = True
        self.grid = [
            [Cell(1,'letter') for _ in range (15) ]
            for _ in range (15)
        ]

    def validate_empty(self):
        if self.grid[7][7] is not None:
            self.is_empty = False
        return self.is_empty

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

    def put_words(self, word, location, orientation):
        len_word = len(word)
        pos_x = location[0]
        pos_y = location[1]
        if orientation == 'H':
            for i in range (len_word):
                self.grid[pos_x][pos_y + i].add_letter(word[i])
        else:
            for i in range (len_word):
                self.grid[pos_x + i][pos_y].add_letter(word[i])

    def validate_word_place_board(self,word,location,orientation):
        center_of_board = (7, 7)
        for i in range(len(word)):
            pos_x = location[0] + i if orientation == "H" else location[0] #si es h, va sumando i horizontalmente
            pos_y = location[1] + i if orientation == "V" else location[1] # idem vertical
            print(f"posicion ({pos_x}, {pos_y}) de letra '{word[i]}'")
            if pos_x == center_of_board[0] and pos_y == center_of_board[1]: # si x e y son 7,7
                print ("pasa por el centro")
                return True
        return False