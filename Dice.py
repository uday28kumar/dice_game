import random
import uuid


class Dice:
    def __init__(self):
        self.id = uuid.uuid4()
        self.numbers = [1, 2, 3, 4, 5, 6]

    def roll(self):
        return random.randint(1, 6)
