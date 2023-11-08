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


    @patch('builtins.input', side_effect=3)
    def test_option_3(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        with patch.object(ScrabbleCli, 'exchange_tiles') as mock_exchange_tiles:
            cli = ScrabbleCli()
            cli.game = scrabble_game
            cli.option_chosen(3)
            mock_exchange_tiles.assert_called_once()

    @patch('builtins.input', side_effect='N')
    def test_option_3N(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        with patch.object(ScrabbleCli, 'exchange_tiles') as mock_exchange_tiles:
            cli = ScrabbleCli()
            cli.game = scrabble_game
            cli.option_chosen('N')
            mock_exchange_tiles.assert_not_called()



if __name__ == '__main__':
    unittest.main()