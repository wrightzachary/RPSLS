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
        print('')
        print("Instructions:")
        print("Pick a gesture! Gesture options are: Rock, Paper, Scissors, Lizard, Spock")
        print('')
        print("Rules are: ")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print('')

    def choose_game_mode(self):
        number_of_players = input("How many players?")
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
        while self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Round tie!")
            return

        while self.player_one.chosen_gesture == "rock":
            if self.player_two.chosen_gesture == "scissors":
                print("Player_one wins! Rock breaks Scissors")
            else:
                print("Player_two wins!")
            return

        while self.player_one_turn == "paper":
            if self.player_two_turn == "rock":
                print("Player_one wins! Paper covers Rock!")
            else:
                print("Player_two wins!")
            return

        while self.player_one_turn == "scissors":
            if self.player_two_turn == "paper":
                print("Player_one wins! Scissors cut Paper!")
            else:
                print("player_two wins!")
            return

        while self.player_one_turn == "rock":
            if self.player_two_turn == "lizard":
                print("Player_one wins! Rock crushes Lizard!")
            else:
                print("player_two wins!")
            return

        while self.player_one_turn == "lizard":
            if self.player_two_turn != "spock":
                print("player_two wins!")
            else:
                print("Player_one wins! Lizard poisons Spock!")
            return

        while self.player_one_turn == "spock":
            if self.player_two_turn == "scissors":
                print("Player_one wins! Spock smashes Scissors!")
            else:
                print("player_two wins!")
            return

        while self.player_one_turn == "scissors":
            if self.player_two_turn == "lizard":
                print("Player_one wins! Scissors decapitates lizard!")
            else:
                print("player_two wins!")
            return

        while self.player_one_turn == "lizard":
            if self.player_two_turn == "paper":
                print("Player_one wins! Lizard eats Paper!")
            else:
                print("player_two wins!")
            return

        while self.player_one_turn == "paper":
            if self.player_two_turn == "spock":
                print("Player_one wins! paper disproves Spock!")
            else:
                print("player_two wins!")
            return

        while self.player_one_turn == "spock":
            if self.player_two_turn == "rock":
                print("Player_one wins! Spock vaporizes Rock!")
            else:
                print("player_two wins!")
            return

    def computer_turn(self):
        pass

    def display_winner(self):
        print("We have a winner!")
