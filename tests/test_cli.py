from game.scrabblecli import *
from game.board import Board
from unittest.mock import patch
import unittest



class TestCLI(unittest.TestCase):

    def test_show_board(self):
        self.cli = ScrabbleCli()
        board = self.cli.game.board
        self.cli.game.board.set_board()

    def test_status_active(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.status_playing()
        self.assertEqual(scrabblecli.game.current_status, 'playing')

    def test_status_noactive(self):
        scrabblecli = ScrabbleCli()
        scrabblecli.stopped_playing()
        self.assertEqual(scrabblecli.game.current_status, 'not playing')

if __name__ == '__main__':
    unittest.main()