from player import Player
from computer import Computer
player_one_score = 0
player_two_score = 0


class Game:
    def __init__(self):
        self.player_one = Player("Player 1")
        self.player_two = Player("Player 2")
        self.computer = Computer()

    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.set_player_one_name()
        self.set_player_two_name()
        self.player_one_turn()
        self.player_two_turn()
        self.computer_turn()
        self.determining_round_winner()
        self.display_scoreboard()
        self.check_if_game_winner()

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
        game_type = input("Type 1 for single player or 2 for multiplayer")
        return game_type

    def set_player_one_name(self):
        self.name = input("Player one, please enter a name")
        print(f'Hello, {self.name}!')
        return self.name

    def set_player_two_name(self):
        self.name2 = input("Player two, please enter a name")
        print(f'Hello, {self.name2}!')
        return self.name2

    def player_one_turn(self):
        self.player_one.chosen_gesture = input(f'Enter your gesture, {self.name}')

    def player_two_turn(self):
        self.player_two.chosen_gesture = input(f'Enter your gesture, {self.name2}')

    def computer_turn(self):
        pass

    def determining_round_winner(self):
        global player_one_score
        global player_two_score
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Round tie!")
            return
        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "scissors":
            print("Player_one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "paper" and self.player_two_turn == "rock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "scissors" and self.player_two_turn == "paper":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "rock" and self.player_two_turn == "lizard":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "lizard" and self.player_two_turn != "spock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "spock" and self.player_two_turn == "scissors":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "scissors" and self.player_two_turn == "lizard":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "lizard" and self.player_two_turn == "paper":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "paper" and self.player_two_turn == "spock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "spock" and self.player_two_turn == "rock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        else:
            print(f"{self.name2} wins the round!")
            player_two_score += 1
        return

    def display_scoreboard(self):
        print(f"{self.name}: {player_one_score}")
        print(f"{self.name2}: {player_two_score}")

    def check_if_game_winner(self):
        global player_one_score
        global player_two_score
        if player_one_score == 2:
            print(f"{self.name} wins the game!")
        elif player_two_score == 2:
            print(f"{self.name2} wins the game!")

        else:
            self.run_game()
