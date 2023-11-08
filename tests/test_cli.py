from game.scrabblecli import *
from game.board import *
from game.player import *
from game.scrabble import *
from unittest.mock import patch, Mock, MagicMock
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


    @patch('builtins.input', side_effect=1)
    def test_option_1(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        with patch.object(ScrabbleCli, 'place_word') as mock_place_word:
            cli = ScrabbleCli()
            cli.game = scrabble_game
            cli.option_chosen(1)
            mock_place_word.assert_called_once()

    @patch('game.scrabble.BagTiles.joker_value')
    def test_option_2(self, mock_joker_value):
        scrabble_game = ScrabbleGame(players_count=2)
        cli = ScrabbleCli()
        cli.game = scrabble_game
        cli.option_chosen(2)
        mock_joker_value.assert_called_once()

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

    @patch('builtins.input', side_effect=['4'])
    def test_option_4(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        cli = ScrabbleCli()
        cli.game = scrabble_game

        cli.game.next_turn = unittest.mock.MagicMock()
        cli.option_chosen(4)
        cli.game.next_turn.assert_called_once()

    @patch('builtins.input', side_effect=5)
    def test_option_5(self, mock_input):
        scrabble_game = ScrabbleGame(players_count=2)
        with patch.object(ScrabbleCli, 'finish_game') as mock_finish_game:
            cli = ScrabbleCli()
            cli.game = scrabble_game
            cli.option_chosen(5)
            mock_finish_game.assert_called_once()


if __name__ == '__main__':
    unittest.main()