class Player:
    def __init__(self, average, name, handedness):
        self.average = average
        self.name = name
        self.handedness = handedness
    def __repr__(self):
        return self.name