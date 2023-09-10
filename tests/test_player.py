import unittest
from game.scrabble import Player

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


if __name__ == '__main__':
    unittest.main