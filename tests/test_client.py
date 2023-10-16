from game.client import *
from unittest.mock import patch
import unittest


# class TestMain(unittest.TestCase):
#         @patch('builtins.print')
#         @patch('game.cli.show_player')
#         @patch('game.cli.show_board')
#         @patch('game.cli.get_player_count', return_value=3)
#         @patch('game.cli.get_inputs', return_value=((1, 3), 'H', 'CASA'))
#         @patch.object(ScrabbleGame, 'is_playing', side_effect=[True, False])
#         @patch.object(ScrabbleGame, 'get_current_player', return_value=(0, "Player",))
#         @patch.object(ScrabbleGame, 'play')
#         def test_main(self, *args):
#             main()

class TestCLI(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(
            get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(
            get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        self.assertEqual(
            get_player_count(),
            1,
        )


if __name__ == '__main__':
    unittest.main()