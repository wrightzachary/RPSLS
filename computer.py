import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__(Player)

    def get_random_gesture(self, player_name):
        random_number = random.randint(0, 5)
        random_gesture = self.gestures[random_number]
        print(f'{player_name} chose {random_gesture}')
