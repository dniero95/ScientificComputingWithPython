import copy
import random
# Consider using the modules imported above.

class Hat:

    # Here I store all Hats
    all: list = []
    def __init__(self, **kwargs):
        self.balls = []
        for key, value in kwargs.items():
            for index in range(value):
                self.balls.append(key)

        # check if at least one ball has been passed
        assert len(self.balls) >= 1, f'Insert at least one ball'

        Hat.all.append(self)

    # This method draw from the hat a number of balls at random

    def draw(self, number_of_balls:int):
        drawn: list = []
        for index in range(number_of_balls):
            draw = random.choice(self.balls)
            self.balls.remove(draw)
            drawn.append(draw)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass