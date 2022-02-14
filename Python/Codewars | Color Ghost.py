import random

class Ghost(object):
    def __init__(self):
        col = "white", "yellow", "purple", "red"
        self.color = random.choice(col)
