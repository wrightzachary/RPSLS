from player import Player
from playertwo import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = input()
        pass

    def run_game(self):
        self.display_welcome()
        # instructions
        # choose game mode - Single or Multi
        self.rounds()
        # player one chooses gesture
        # player two chooses gesture
        # determine winner, score increases for winner
        # loop to continue gameplay for best out of 3
        self.display_winner()
        # prompt to play again - not mvp

    def display_welcome(self):
        print("Welcome to RPSLS!")
        print('')
        print("Single player or multiplayer?")

    def choose_game_mode(self):
        input("How many PLayers?")
        if input == 2:
            self.player_two = Human()
        else:
            self.player_two = AI()

    def players(self):
        pass
        # determine if it is human vs AI or human vs human

    def rounds(self):
        pass

    def player_turn(self):
        pass

    def player2_turn(self):
        pass

    def computer_turn(self):
        pass

    def display_winner(self):
        print("We have a winner!")
