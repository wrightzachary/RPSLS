import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__(Player)
        self.computer_name = "The Machine"

    def get_random_gesture(self, player_name):
        random_number = random.randint(0, len(self.gestures)-1)
        random_gesture = self.gestures[random_number]
        print(f'{self.computer_name} chose {random_gesture}')
