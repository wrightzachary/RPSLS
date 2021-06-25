from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__(Player)
        self.chosen_gesture = ""
        self.set_computer_name()

    def set_computer_name(self):
        self.name = "The Machine"

    def get_random_gesture(self, player_name):
        random_gesture = random.randint(0, len(self.gestures)-1)
        computer_gesture = self.gestures[random_gesture]
        self.chosen_gesture = computer_gesture
