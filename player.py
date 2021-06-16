class Player:
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def name(self):
        input("Enter your name:")

    def choose_gesture(self):

