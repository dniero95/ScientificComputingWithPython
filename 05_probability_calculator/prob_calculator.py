import copy
import random
# Consider using the modules imported above.

class Hat:

    # Here I store all Hats
    all: list = []
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for index in range(value):
                self.contents.append(key)

        # check if at least one ball has been passed
        assert len(self.contents) >= 1, f'Insert at least one ball'

        Hat.all.append(self)

    # This method draw from the hat a number of balls at random

    def draw(self, number_of_balls:int):
        drawn: list = []
        # handle if you draw a nuber of balls equals or more than the balls in the hat
        if number_of_balls >= len(self.contents):
            drawn.extend(self.contents)
            self.contents.clear()
            return drawn

        for index in range(number_of_balls):

            draw = random.choice(self.contents)
            self.contents.remove(draw)
            drawn.append(draw)
        return drawn

def experiment(hat:Hat, expected_balls:dict, num_balls_drawn:int, num_experiments:int):
    success = 0
    for index in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)

        draw = experiment_hat.draw(num_balls_drawn)
        outcome = True
        for key, value in expected_balls.items():
            if value > draw.count(key):
                outcome = False

        if  outcome:
            success += 1
            # print(success)
    result = success/num_experiments
    return result

