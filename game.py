from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Human("Zach")
        self.player_two = Human("Alec")

    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.rounds()
        # player one chooses gesture
        # player two chooses gesture
        # determine winner, score increases for winner
        # loop to continue gameplay for best out of 3
        self.display_winner()
        # prompt to play again - not mvp

    def display_welcome(self):
        print("Welcome to RPSLS!")
        print("Instructions")
        print("Rock crushes Scissors, "
              f"Scissors cuts Paper, "
              f"Paper covers Rock, "
              f"Rock crushes Lizard")
        print("Lizard poisons Spock, "
              f"Spock smashes Scissors, "
              f"Scissors decapitates Lizard")
        print("Lizard eats Paper, "
              f"Paper disproves Spock, "
              f"Spock vaporizes Rock")

    def choose_game_mode(self):
        number_of_players = input("How many Players?")
        if number_of_players == 2:
            self.player_two = Human("Alec")
        else:
            self.player_two = Computer()

    # def players(self, player_one, player_two):
    #     self.player_one = player_one
    #     self.player_two = player_two

    def rounds(self):
         pass

    def player_one_turn(self):
        pass

    def player_two_turn(self):
        pass

    def computer_turn(self):
        pass

    def display_winner(self):
        print("We have a winner!")

    def player(self):
        pass
