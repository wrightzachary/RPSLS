from player import Player
import random
n = 1


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        for i in range(n):
            print(random.choice(self.gestures), end=" ")
