from human import Human
from computer import Computer
player_one_score = 0
player_two_score = 0


class Game:
    def __init__(self):
        self.computer = Computer()
        self.player_one = Human("Player 1")
        self.player_two = Human("Player 2")
        self.display_welcome()
        self.choose_game_mode()

    def run_game(self):
        self.player_one_turn()
        self.player_two_turn()
        self.determining_round_winner()
        self.display_scoreboard()
        self.check_if_game_winner()
        #  score increases for winner
        # loop to continue gameplay for best out of 3
        self.game_over()

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
        print("How many players?")
        number_of_players = input()
        # if number_of_players == 2:
        #     self.player_two = Human("Player 2")
        if number_of_players == 1:
            self.player_two = Computer()
        else:
            self.player_two = Computer()

    def players(self, player_one, computer, player_two):
        self.player_one = player_one
        self.computer = computer
        self.player_two = player_two

    def player_one_turn(self):
        print("Player one, enter your gesture:")
        self.player_one.chosen_gesture = input()

    def player_two_turn(self):
        print("Player two, enter your gesture:")
        self.player_two.chosen_gesture = input()

    def determining_round_winner(self):
        global player_one_score
        global player_two_score
        while self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Round tie!")
            return

        while self.player_one.chosen_gesture == "rock":
            if self.player_two.chosen_gesture == "scissors":
                print("Player_one wins! Rock breaks Scissors")
                player_one_score += 1
            else:
                print("Player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "paper":
            if self.player_two_turn == "rock":
                print("Player_one wins! Paper covers Rock!")
                player_one_score += 1
            else:
                print("Player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "scissors":
            if self.player_two_turn == "paper":
                print("Player_one wins! Scissors cut Paper!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "rock":
            if self.player_two_turn == "lizard":
                print("Player_one wins! Rock crushes Lizard!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "lizard":
            if self.player_two_turn != "spock":
                print("player_one wins! Lizard poisons Spock!")
                player_one_score += 1
            else:
                print("Player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "spock":
            if self.player_two_turn == "scissors":
                print("Player_one wins! Spock smashes Scissors!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "scissors":
            if self.player_two_turn == "lizard":
                print("Player_one wins! Scissors decapitates lizard!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "lizard":
            if self.player_two_turn == "paper":
                print("Player_one wins! Lizard eats Paper!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "paper":
            if self.player_two_turn == "spock":
                print("Player_one wins! paper disproves Spock!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

        while self.player_one_turn == "spock":
            if self.player_two_turn == "rock":
                print("Player_one wins! Spock vaporizes Rock!")
                player_one_score += 1
            else:
                print("player_two wins!")
                player_two_score += 1
            return

    def display_scoreboard(self):
        print(f"Player_one score: {player_one_score}")
        print(f"player_two score: {player_two_score}")

    def check_if_game_winner(self):
        global player_one_score
        global player_two_score
        if player_one_score == 2:
            print("Player_one wins the game!")
        elif player_two_score == 2:
            print("Player_two wins the game!")

    def game_over(self):
        user_choice = input("Do you want to play again? (y/n)")
        if user_choice in ["Y", "y", "yes", "Yes"]:
            self.run_game()
        if user_choice in ["N", "n", "no", "No"]:
            print("See you again!")

    def computer_turn(self):
        pass
