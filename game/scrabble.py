import random

class InvalidWordException:
    pass
class InvalidPlaceWordException:
    pass

class Tile:
    def __init__(self,letter,value):
        self.letter = letter
        self.value = value

    def __repr__(self):
        return self.letter

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
            Tile('C',3),
            Tile('M',3),
            Tile('M',3),
            Tile('P',3),
            Tile('P',3),
            Tile('F',4),
            Tile('H',4),
            Tile('H',4),
            Tile('H',4),
            Tile('V',4),
            Tile('Y',4),
            Tile('Q',5),
            Tile('J',8),
            Tile('Ñ',8),
            Tile('X',8),
            Tile('Z',10),
            Tile('#',None),
            Tile('#',None),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self,tiles):
        self.tiles.extend(tiles)


    def get_tile_value(self, letter):
        for tile in self.tiles:
            if tile.letter == letter:
                return tile.value

    def joker_value(self):
        if "#" in [tile.letter for tile in self.tiles]:
            joker_val = input("Please enter the letter value of the # tile: ")
            for tile in self.tiles:
                if tile.letter == '#':
                    tile.value = self.get_tile_value(joker_val.upper())
                    break


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

        for cell in word:
            if cell.multiplier_type == 'letter':
                total_value += cell.calculate_letter_value()
            elif cell.multiplier_type == 'word':
                total_value += cell.calculate_letter_value()
                word_multiplier *= cell.multiplier
            else:
                total_value += cell.letter.value
        total_value *= word_multiplier
        return total_value