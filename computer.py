import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__("Machine")

    def get_random_gesture(self):
        print(f'Computer chose {random.choice(self.gestures)}')
