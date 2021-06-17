from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Human("Player 1")
        self.player_two = Human("Player 2")

    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.player_one_turn()
        self.player_two_turn()
        self.determining_round_winner()
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
            self.player_two = Human("Player 2")
        else:
            self.player_two = Computer()

    def players(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def player_one_turn(self):
        print("Enter your gesture:")
        self.player_one.chosen_gesture = input()

    def player_two_turn(self):
        print("Enter your gesture:")
        self.player_two.chosen_gesture = input()

    def determining_round_winner(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Round tie!")
        elif self.player_one.chosen_gesture == "rock":
            if self.player_two.chosen_gesture == "scissors":
                print("Player_one wins! Rock breaks Scissors")
            else:
                print("Player_two wins!")

        # elif self.player_one_turn == "paper":
        #     if self.player_two_turn == "rock":
        #         print("Player_one wins!Paper covers Rock!")
        #     else:
        #         print("Player_two wins!")
        #
        # elif self.player_one_turn == "scissors":
        #     if self.player_two_turn == "paper":
        #         print("Player_one wins! Scissors cut Paper!")
        #     else:
        #         print("player_two wins!")

    def computer_turn(self):
        pass

    def display_winner(self):
        print("We have a winner!")
