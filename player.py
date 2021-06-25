class Player:
    def __init__(self, name):
        self.name = name
        self.chosen_gesture = ""
        self.score = 0
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def choose_gesture_player(self):
        gesture_input = input(f'{self.name} Enter gesture')
        for gesture in self.gestures:
            if gesture_input.lower() == gesture.lower():
                self.chosen_gesture = gesture
            else:
                print(f'Input not valid, please retry')
                self.choose_gesture_player()

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gestures:
            print(each)
            gesture_index += 1
