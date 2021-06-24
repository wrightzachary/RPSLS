class Game:
    def __int__(self):
        self.player_one = ""
        self.player_two = ""

    def run_game(self):
        self.instructions()
        self.choose_game_mode()
        self.player_one_chosen_gesture()
        self.player_two_chosen_gesture()
        self.game_start()
        self.winner_announced()
        self.another_round()

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
