class EntireGame:
    lineup = []
    inning = 1
    outs = 0
    firstBase = ""
    secondBase = ""
    thirdBase = ""
    score = 0
    currentBatter = 0
    for i in range(0, 9):
        lineup.append(input("Enter batter name: ").capitalize())
    print(lineup)

    #### Print Info ####

    def printInfo(self):

        if self.firstBase != "":
            print(self.firstBase, "is on first")
        else:
            print("There is no one on first")
        if self.secondBase != "":
            print(self.secondBase, "is on second")
        else:
            print("There is no one on second")
        if self.thirdBase != "":
            print(self.thirdBase, "is on third")
        else:
            print("There is no one on third")
        print("The score is: " + str(self.score))
        print("There are", self.outs, "outs")
        print("The current batter is", self.lineup[self.currentBatter])
        print("It is currently the", self.inning, "inning")

    #### End Print Info ####

    def doSingle(self):
        if self.thirdBase != "":
            self.score += 1 # same as score = score + 1
            self.thirdBase = ""
        if self.secondBase != "":
            self.thirdBase = self.secondBase
            self.secondBase = ""
        if self.firstBase != "":
            self.secondBase = self.firstBase
        self.firstBase = self.lineup[self.currentBatter]

    def doDouble(self):
        if self.thirdBase != "":
            self.score += 1
            self.thirdBase = ""
        if self.secondBase != "":
            self.score += 1
        if self.firstBase != "":
            self.thirdBase = self.firstBase
            self.firstBase = ""
        self.secondBase = self.lineup[self.currentBatter]

    def doTriple(self):
        if self.thirdBase != "":
            self.score += 1
            self.thirdBase = ""
        if self.secondBase != "":
            self.score +=1
            self.secondBase = ""
        if self.firstBase != "":
            self.score +=1
            self.firstBase = ""
        self.thirdBase = self.lineup[self.currentBatter]

    def doHomeRun(self):
        if self.thirdBase != "":
            self.score += 1
            self.thirdBase = ""
        if self.secondBase != "":
            self.score += 1
            self.secondBase = ""
        if self.firstBase != "":
            self.score += 1
            self.firstBase = ""
        self.score +=1

    def doOut(self):
        self.outs += 1
        if self.outs == 3:
            self.thirdBase = ""
            self.secondBase = ""
            self.firstBase = ""
            self.inning += 1
            self.outs = 0

    def atBat(self):
        self.printInfo()
        result = input("What did the batter do?").lower()
        if result == "s":
            self.doSingle()
        elif result == "d":
            self.doDouble()
        elif result == "t":
            self.doTriple()
        elif result == "hr":
            self.doHomeRun()
        else:
            self.doOut()
        self.currentBatter += 1

entireGame = EntireGame()
entireGame.atBat()
entireGame.atBat()
entireGame.atBat()
entireGame.printInfo()
