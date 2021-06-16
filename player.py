class Player:
    def __init__(self, name):
        self.name = name
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def player_name(self):
        input("Enter your name:")

    def choose_gesture(self):
        input([self.gestures])
