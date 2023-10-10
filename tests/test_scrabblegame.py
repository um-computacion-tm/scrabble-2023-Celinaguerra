import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame, Dictionary, Board

class TestScrabbleGame(unittest.TestCase):
    def test__init__(self):
        scrabble_game = ScrabbleGame(players_count = 3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),3)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_isnt_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_game_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

#NO RECONOCE get_player_count
# class TestCLI(unittest.TestCase):
#     @patch('builtins.input', return_value='3')
#     def test_get_player_count(self, input_patched):
#         self.assertEqual(
#             get_player_count(),
#             3,
#         )

#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['A', '3'])
#     def test_get_player_count_wrong_input(self, input_patched, print_patched):
#         self.assertEqual(
#             get_player_count(),
#             3,
#         )

#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['10', '1'])
#     def test_get_player_count_control_max(self, input_patched, print_patched):
#         self.assertEqual(
#             get_player_count(),
#             1,
#         )
