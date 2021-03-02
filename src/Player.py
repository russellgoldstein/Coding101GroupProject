class Player:
    def __init__(self, name, hitChance):
        self.name = name
        self.hitChance = hitChance

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Player):
            # don't attempt to compare against unrelated types
            return False

        return self.name == other.name and self.hitChance == other.hitChance