from game.scrabblegame import *
from game.scrabble import *
from game.board import *
from game.player import *
from game.dictionary import *

class ScrabbleCli:
    def __init__(self):
        self.game = ScrabbleGame(players_count=2)
        self.status_playing()
        self.take_starting_tiles()
        self.game.next_turn()

    def play_turn(self):
        while self.game.current_status == 'playing':
            for i in range(len(self.game.players)):
                self.game.board.set_board()
                current_player = self.game.current_player
                print(f'Its your turn {current_player}!')
                print(f'Score: {self.game.show_score()[current_player]}')
                print(f'These are your current tiles: {current_player.show_tiles()}')
                option = int(input("What you wish to do?: \n1) Place a word \n2) Use the Joker a letter \n3) Exchange tiles \n4) Skip turn\n5) Quit the game \nChoice: "))
                self.option_chosen(option)

    def option_chosen(self,option):
        if option == 1:
            self.place_word()

        elif option == 2:
            self.game.bag_tiles.joker_value()

        elif option == 3:
            self.exchange_tiles()
        
        elif option == 4:
            self.game.next_turn()
        
        elif option == 5:
            self.finish_game()



    def status_playing(self):
        self.game.current_status = 'playing'

    def stopped_playing(self):
        self.game.current_status = 'not playing'

    def take_starting_tiles(self):
        for player in self.game.players:
            player.refill(self.game.bag_tiles)

    def exchange_tiles(self):
        print(f'{self.game.current_player} Your tiles:')
        print(self.game.current_player.show_tiles())
        print('Enter the positions of the tiles you wanna exchange. press N to quit')
        positions = input()
        if positions == 'N':
            self.play_turn()
            return False
        positions = positions.split(',')
        positions = [int(position) for position in positions]
        new_tiles = self.game.bag_tiles.take(len(positions))
        old_tiles = self.exchange_tiles(positions)
        self.game.bag_tiles.put(old_tiles)
        print('The following tiles have been exchanged: ')
        print(self.game.current_player.show_tiles())
        print('Press any key to continue')
        input()
        return True

    def place_word(self, word, location, orientation):
        word = input("Enter the word you want to play: ").upper()
        location = tuple(map(int, input("Enter the location (row, column): ").split(',')))
        orientation = input("Enter the orientation (H for horizontal, V for vertical): ").upper()

        try:
            if not self.game.current_player.has_letters(word):
                raise Exception("You don't have the required letters to form this word.")
            if not self.game.dic.valid_word(word):
                raise Exception("The word is not valid according to the dictionary.")

            if self.game.current_player == self.game.players[0] and self.game.board.validate_empty():
                if location != (7, 7):
                    raise Exception("In the first turn, the word must pass through the center (7, 7).")
                self.game.board.put_words(word, location, orientation)
            else:
                if not self.game.board.validate_word_inside_board(word, location, orientation):
                    raise Exception("Invalid word placement on the board.")
                if not self.game.board.validate_word_place_board(word, location, orientation):
                    raise Exception("The word is not properly placed on the board.")
                self.game.board.put_words(word, location, orientation)

            words = self.game.board.put_words(word, location, orientation)
            total = self.game.cell.calculate_word_value(words)
            self.game.current_player.increase_score(total)
            self.game.current_player.refill(self.game.bag_tiles)
            self.game.next_turn()

        except Exception as e:
            print(f"Error: {e}")

    def finish_game(self):
        stop_game = input("Are you sure you want to stop the game (Y/N)? ").strip().lower()
        if stop_game == 'y':
            self.stopped_playing()
            scores = self.game.show_score()
            max_score = max(scores.values())
            winners = [player for player, score in scores.items() if score == max_score]
            if len(winners) == 1:
                print(f"Player {winners[0]} wins with {max_score} points!")
            else:
                print("It's a tie! The following players share the highest score:")
                for winner in winners:
                    print(f"Player {winner}: {max_score} points")
