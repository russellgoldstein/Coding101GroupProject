import random

lineup = ["Nimmo", "McNeil", "Lindor", "Conforto", "Alonso", "Smith", "Davis", "McCann", "deGrom"]
hitChance = [.260, .305, .315, .333, .240, .283, .270, .275, .188]
inning = 1
outs = 0
firstBase = ""
secondBase = ""
thirdBase = ""
ourScore = 0
opponentScore = 0
currentBatter = 0
totalInnings = 9
print(lineup)

#### Print Info ####

def printInfo():
    #Because no variables are being re/assigned a value in this function, the Python interpretor assumes global by default
    print("----------------------------------------------------------")
    if firstBase != "":
        print(firstBase, "is on first")
    else:
        print("There is no one on first")
    if secondBase != "":
        print(secondBase, "is on second")
    else:
        print("There is no one on second")
    if thirdBase != "":
        print(thirdBase, "is on third")
    else:
        print("There is no one on third")
    print("Our score is: " + str(ourScore) +" and the opponent's score is "+ str(opponentScore))
    print("There are", outs, "outs")
    print("The current batter is", lineup[currentBatter], "and his batting average is", hitChance[currentBatter])
    print("It is currently the", inning, "inning")

#### End Print Info ####

def doSingle():
    global thirdBase, secondBase, firstBase, ourScore
    print(lineup[currentBatter] + " got a single")
    if thirdBase != "":
        ourScore += 1 # same as score = score + 1
        print(thirdBase + " scored!")
        thirdBase = ""
    if secondBase != "":
        thirdBase = secondBase
        secondBase = ""
    if firstBase != "":
        secondBase = firstBase
    firstBase = lineup[currentBatter]

def doDouble():
    global thirdBase, secondBase, firstBase, ourScore
    print(lineup[currentBatter] + " got a double")
    if thirdBase != "":
        ourScore += 1
        print(thirdBase + " scored!")
        thirdBase = ""
    if secondBase != "":
        ourScore += 1
        print(secondBase + " scored!")
    if firstBase != "":
        thirdBase = firstBase
        firstBase = ""
    secondBase = lineup[currentBatter]

def doTriple():
    global thirdBase, secondBase, firstBase, ourScore
    print(lineup[currentBatter] + " got a triple")
    if thirdBase != "":
        ourScore += 1
        print(thirdBase + " scored!")
        thirdBase = ""
    if secondBase != "":
        ourScore +=1
        print(secondBase + " scored!")
        secondBase = ""
    if firstBase != "":
        ourScore +=1
        print(firstBase + " scored!")
        firstBase = ""
    thirdBase = lineup[currentBatter]

def doHomeRun():
    global thirdBase, secondBase, firstBase, ourScore
    print(lineup[currentBatter] + " got a home run")
    if thirdBase != "":
        ourScore += 1
        print(thirdBase + " scored!")
        thirdBase = ""
    if secondBase != "":
        ourScore += 1
        print(secondBase + " scored!")
        secondBase = ""
    if firstBase != "":
        ourScore += 1
        print(firstBase + " scored!")
        firstBase = ""
    ourScore +=1

def doOut():
    global outs, thirdBase, secondBase, firstBase, inning
    print(lineup[currentBatter] + " got an out")
    outs += 1
    if outs == 3:
        thirdBase = ""
        secondBase = ""
        firstBase = ""
        inning += 1
        outs = 0
        opponentScoring()

def whatHit():
    if (hitChance[currentBatter] * 1000) >= random.randint(0, 1001):
        whichHit = random.randint(0, 20)
        if whichHit > 6:
            doSingle()
        elif whichHit > 3:
            doDouble()
        elif whichHit > 1:
            doTriple()
        else:
            doHomeRun()
    else:
        doOut()

def atBat():
    global currentBatter
    whatHit()
    currentBatter += 1
    if currentBatter > 8:
        currentBatter = 0

def opponentScoring():
    global opponentScore
    thisInningRuns = 0
    if random.randint(0, 3) == 0:
        thisInningRuns = random.randint(1, 5)
        opponentScore = opponentScore + thisInningRuns
    print("The opponent scored", thisInningRuns, "runs ")




while inning <= totalInnings or opponentScore == ourScore:
    atBat()

if ourScore > opponentScore:
    print("Our team won "+str(ourScore)+" to "+str(opponentScore))
else:
    print("Our team lost "+str(ourScore)+" to "+str(opponentScore))

