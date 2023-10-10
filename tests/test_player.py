import unittest
from game.scrabble import Player, BagTiles, Tile

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player1 = Player()
        self.assertEqual(len(player1.tiles),0)

    def test_take_tiles(self):
        player=Player()
        bag = BagTiles()
        player.take_tiles(bag, 7)
        self.assertEqual(len(player.tiles), 7)

    def test_set_name(self):
        player = Player()
        player.set_name('Celi')
        self.assertEqual(player.get_name(), 'Celi')

    def test_score(self):
        player = Player()
        player.increase_score(3)
        self.assertEqual(player.get_score(), 3)

    def test_refill(self):
        #jugador con menos de 7 fichas
        player2 = Player()
        player2.tiles = ['A', 'B']
        bag = BagTiles()
        player2.refill(bag)
        self.assertEqual(len(player2.tiles), 7)

    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        player.tiles = bag_tile.tiles 
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)


    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        player.tiles = bag_tile.tiles
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main