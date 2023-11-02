import unittest
from game.scrabblegame import ScrabbleGame

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

    def test_show_scores(self):
        scrabble_game = ScrabbleGame(players_count=1)
        scrabble_game.players[0].set_name('Celi')
        self.assertEqual(scrabble_game.show_score(), {'Celi':0})

    def test_status_active(self):
        scrabble_game = ScrabbleGame(players_count=1)
        scrabble_game.playing()
        self.assertEqual(scrabble_game.current_status, 'playing')

    def test_status_notactive(self):
        scrabble_game = ScrabbleGame(players_count=1)
        scrabble_game.stopped_playing()
        self.assertEqual(scrabble_game.current_status, 'not playing')