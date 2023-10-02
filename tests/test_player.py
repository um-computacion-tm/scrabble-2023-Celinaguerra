import unittest
from game.scrabble import Player
#clase
from game.scrabble import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player1 = Player(id=1, name='celi')
        self.assertEqual(
            len(player1.tiles),
            7,
        )

    def test_get_name(self):
        player1 = Player(id=1, name=None)
        self.name = 'celi'
        self.assertEqual(player1.set_name('celi'), 'celi')


####

    def test_refill(self):
        #jugador con menos de 7 fichas
        player2 = Player(id=2,name=None)
        player2.tiles = ['A', 'B']
        bag = BagTiles()
        bag.take(5)
        player2.refill(bag)
        self.assertEqual(len(player2.tiles), 7)

if __name__ == '__main__':
    unittest.main