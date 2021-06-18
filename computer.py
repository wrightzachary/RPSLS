import random
from player import Player

n = 1


class Computer(Player):
    def __init__(self):
        super().__init__(Player)

    def choose_gesture(self):
        for i in range(n):
            print(random.choice(self.gestures), end=" ")
