class Team:
    def __init__(self, name, player1, player2, player3, player4, player5, player6, player7, player8, player9):
        self.name = name
        self.score = 0
        self.lineup = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
        self.currentBatter = 0

    def getCurrentBatterName(self):
        return self.lineup[self.currentBatter].name

    def getCurrentBatterHitChance(self):
        return self.lineup[self.currentBatter].hitChance