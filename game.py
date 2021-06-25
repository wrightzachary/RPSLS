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

    @staticmethod
    def instructions():
        print("Welcome to Rock Paper Scissors Lizard Spock")
        print('')
        print("The rules for Rock-Paper-Scissors-Lizard-Spock:")
        print('')
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

    def choose_game_mode(self):
        pass

    def set_player_one_name(self):
        pass

    def set_player_two_name(self):
        pass

    def player_one_turn(self):
        pass

    def player_one_chosen_gesture(self):
        pass

    def player_two_chosen_gesture(self):
        pass

    def game_start(self):
        pass

    def winner_announced(self):
        pass

    def another_round(self):
        pass
