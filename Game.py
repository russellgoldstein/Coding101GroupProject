import random
class Game:

    def __init__(self, ourTeam):
        self.inning = 1
        self.outs = 0
        self.firstBase = ""
        self.secondBase = ""
        self.thirdBase = ""
        self.totalInnings = 9
        self.opponentScore = 0
        self.ourTeam = ourTeam

    def doSingle(self):
        print(self.ourTeam.getCurrentBatterName() + " got a single")
        if self.thirdBase != "":
            self.ourTeam.score += 1 # same as score = score + 1
            print(self.thirdBase + " scored!")
            self.thirdBase = ""
        if self.secondBase != "":
            self.thirdBase = self.secondBase
            self.secondBase = ""
        if self.firstBase != "":
            self.secondBase = self.firstBase
        self.firstBase = self.ourTeam.getCurrentBatterName()

    def doDouble(self):
        print(self.ourTeam.getCurrentBatterName() + " got a double")
        if self.thirdBase != "":
            self.ourTeam.score += 1
            print(self.thirdBase + " scored!")
            self.thirdBase = ""
        if self.secondBase != "":
            self.ourTeam.score += 1
            print(self.secondBase + " scored!")
        if self.firstBase != "":
            self.thirdBase = self.firstBase
            self.firstBase = ""
        self.secondBase = self.ourTeam.getCurrentBatterName()

    def doTriple(self):
        print(self.ourTeam.getCurrentBatterName() + " got a triple")
        if self.thirdBase != "":
            self.ourTeam.score += 1
            print(self.thirdBase + " scored!")
            self.thirdBase = ""
        if self.secondBase != "":
            self.ourTeam.score +=1
            print(self.secondBase + " scored!")
            self.secondBase = ""
        if self.firstBase != "":
            self.ourTeam.score +=1
            print(self.firstBase + " scored!")
            self.firstBase = ""
        self.thirdBase = self.ourTeam.getCurrentBatterName()

    def doHomeRun(self):
        print(self.ourTeam.getCurrentBatterName() + " got a home run")
        if self.thirdBase != "":
            self.ourTeam.score += 1
            print(self.thirdBase + " scored!")
            self.thirdBase = ""
        if self.secondBase != "":
            self.ourTeam.score += 1
            print(self.secondBase + " scored!")
            self.secondBase = ""
        if self.firstBase != "":
            self.ourTeam.score += 1
            print(self.firstBase + " scored!")
            self.firstBase = ""
        self.ourTeam.score += 1

    def opponentScoring(self):
        thisInningRuns = 0
        if random.randint(0, 3) == 0:
            thisInningRuns = random.randint(1, 5)
            self.opponentScore = self.opponentScore + thisInningRuns
        print("The opponent scored", thisInningRuns, "runs ")
        print("score is us:", self.ourTeam.score, "them:", self.opponentScore)
        print("----------------------------------------------------")

    def doOut(self):
        print(self.ourTeam.getCurrentBatterName() + " got an out")
        self.outs += 1
        if self.outs == 3:
            print("-----------------Bottom of", self.inning, "-----------------------")
            self.thirdBase = ""
            self.secondBase = ""
            self.firstBase = ""
            self.inning += 1
            self.outs = 0
            self.opponentScoring()

    def whatHit(self):
        if (self.ourTeam.getCurrentBatterHitChance() * 1000) >= random.randint(0, 1001):
            whichHit = random.randint(0, 20)
            if whichHit > 6:
                self.doSingle()
            elif whichHit > 3:
                self.doDouble()
            elif whichHit > 1:
                self.doTriple()
            else:
                self.doHomeRun()
        else:
            self.doOut()

    def atBat(self):
        self.whatHit()
        self.ourTeam.currentBatter += 1
        if self.ourTeam.currentBatter > 8:
            self.ourTeam.currentBatter = 0
