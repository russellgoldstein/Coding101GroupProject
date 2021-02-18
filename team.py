class Team:
    def __init__(self, name, lineup):
        self.name = name
        self.lineup = lineup
        self.score = 0
        self.currentBatter = 0
    def printTeamStats(self):
        print(self.name)
        print(self.lineup)
        print(self.score)

    def getCurrentBatterName(self):
        return self.lineup[self.currentBatter].name

    def getCurrentBatterAvg(self):
        return self.lineup[self.currentBatter].average