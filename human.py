from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name()
        self.chosen_gesture = ""

    def set_name(self):
        self.chosen_gesture = ""

    def choose_gesture(self):
        self.name - input("Enter your name")
