import unittest
from game.scrabble import (Tile, BagTiles)
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A',1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tiled(self):
        tile = Tile('D',2)
        self.assertEqual(tile.letter, 'D')
        self.assertEqual(tile.value, 2)

    def test_tilec(self):
        tile = Tile('C',3)
        self.assertEqual(tile.letter, 'C')
        self.assertEqual(tile.value, 3)

    def test_tilef(self):
        tile = Tile('F',4)
        self.assertEqual(tile.letter, 'F')
        self.assertEqual(tile.value, 4)

    def test_tilerr(self):
        tile = Tile('RR',8)
        self.assertEqual(tile.letter, 'RR')
        self.assertEqual(tile.value, 8)

    def test_tilep(self):
        tile = Tile('P',3)
        self.assertEqual(tile.letter, 'P')
        self.assertEqual(tile.value, 3)

    def test_tilez(self):
        tile = Tile('Z',10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)

    def test_tiley(self):
        tile = Tile('Y',4)
        self.assertEqual(tile.letter, 'Y')
        self.assertEqual(tile.value, 4)

    def test_tilej(self):
        tile = Tile('J',8)
        self.assertEqual(tile.letter, 'J')
        self.assertEqual(tile.value, 8)

    def test_tileq(self):
        tile = Tile('Q',5)
        self.assertEqual(tile.letter, 'Q')
        self.assertEqual(tile.value, 5)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
                100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        tiles = bag.take(5)
        put_tiles = [Tile('Z',1), Tile('Y',1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            97,
        )

    def test_joker_value(self):
        bag = BagTiles()
        bag.tiles = [
            Tile('Y', 4),
            Tile('Q', 5),
            Tile('J', 8),
            Tile('Ñ', 8),
            Tile('X', 8),
            Tile('Z', 10),
            Tile('#', None),
            Tile('#', None)
        ]
        
        # Mock user input to enter the letter 'Q'
        with unittest.mock.patch('builtins.input', return_value='Q'):
            bag.joker_value()

        # Check that the value of '#' has been set to 5
        for tile in bag.tiles:
            if tile.letter == '#':
                self.assertEqual(tile.value, 5)
                break



if __name__ == "__main__":
    unittest.main