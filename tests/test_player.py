import unittest
from game.scrabble import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player1 = Player(id=1)
        self.assertEqual(
            len(player1.tiles),
            7,
        )

if __name__ == '__main__':
    unittest.main