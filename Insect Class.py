import random

class Insect:
    def __init__(self):
        self.wing= 2
        self.legs= 4
        self.flight = 0

    def calc_flight(self):
        self.flight = random.randint(0,10)

    def get_flight(self):
        return self.flight

    