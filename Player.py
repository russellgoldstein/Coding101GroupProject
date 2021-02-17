class Player:
    def __init__(self, name, hitChance):
        self.name = name
        self.hitChance = hitChance

    def __repr__(self):
        return self.name