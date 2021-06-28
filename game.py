from computer import Computer
from human import Human

player_one_score = 0
player_two_score = 0
computer_score = 0


class Game:
    def __init__(self):
        self.player_one = Human(self)
        self.player_two = None
        self.computer = Computer()

    def run_game(self):
        self.game_instructions()
        self.choose_game_mode()

    @staticmethod
    def game_instructions():
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
        response = int(input())
        if response == 1:
            self.name = input("Player one, please enter a name")
            self.player_two = Computer()
            self.game_logic_single_player()
            self.best_out_of_three_single_player()
        elif response == 2:
            self.player_one = Human(self)
            self.player_two = Human(self)
            self.name = input("Player one, please enter a name")
            self.name_other = input("Player two, please enter a name")
            self.game_logic_multiplayer()
            self.best_out_of_three_multiplayer()
        else:
            print("Not a valid number of players")
            Game.choose_game_mode(self)
        return

    def game_logic_multiplayer(self):
        global player_one_score
        global player_two_score
        self.player_one_turn = input(f'Enter your gesture, {self.name}')
        self.player_two_turn = input(f'Enter your gesture, {self.name_other}')
        if self.player_one_turn == self.player_two_turn:
            print("Round tie!")
        elif self.player_one_turn == "rock" and self.player_two_turn == "scissors":
            print("Player_one wins the round!")
            print("The machine wins the round!")
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
            print(f"{self.name_other} wins the round!")
            player_two_score += 1
        self.display_scoreboard_multiplayer()
        return

    def game_logic_single_player(self):
        global player_one_score
        global computer_score
        self.player_one_turn = input(f'Enter your gesture, {self.name}')
        self.computer_turn = Computer.get_random_gesture(self.player_two)
        if self.player_one_turn == self.computer_turn:
            print("Round tie!")
        elif self.player_one_turn == "rock" and self.computer_turn == "scissors":
            print("Player_one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "paper" and self.computer_turn == "rock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "scissors" and self.computer_turn == "paper":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "rock" and self.computer_turn == "lizard":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "lizard" and self.computer_turn != "spock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "spock" and self.computer_turn == "scissors":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "scissors" and self.computer_turn == "lizard":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "lizard" and self.computer_turn == "paper":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "paper" and self.computer_turn == "spock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "spock" and self.computer_turn == "rock":
            print(f"{self.name} wins the round!")
            player_one_score += 1
        else:
            print(f"The Machine wins the round!")
            computer_score += 1
        self.display_scoreboard_single_player()
        return

    def best_out_of_three_multiplayer(self):
        while player_one_score < 2 and player_two_score < 2:
            self.game_logic_multiplayer()
            if player_one_score == 2:
                print(f'{self.name} wins!')
            else:
                print(f'{self.name_other} wins!')

    def best_out_of_three_single_player(self):
        while player_one_score < 2 and computer_score < 2:
            self.game_logic_single_player()
            if player_one_score == 2:
                print(f'{self.name} wins!')
            else:
                print(f'The Machine wins!')

    def display_scoreboard_multiplayer(self):
        print(f"{self.name}: {player_one_score}")
        print(f"{self.name_other}: {player_two_score}")

    def display_scoreboard_single_player(self):
        print(f"{self.name}: {player_one_score}")
        print(f"The Machine: {computer_score}")
