
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

def printInfo():
    #Because no variables are being re/assigned a value in this function, the Python interpretor assumes global by default
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
    print("The score is: " + str(score))
    print("There are", outs, "outs")
    print("The current batter is", lineup[currentBatter])
    print("It is currently the", inning, "inning")

#### End Print Info ####

def doSingle():
    global thirdBase, secondBase, firstBase, score
    if thirdBase != "":
        score += 1 # same as score = score + 1
        thirdBase = ""
    if secondBase != "":
        thirdBase = secondBase
        secondBase = ""
    if firstBase != "":
        secondBase = firstBase
    firstBase = lineup[currentBatter]

def doDouble():
    global thirdBase, secondBase, firstBase, score
    if thirdBase != "":
        score += 1
        thirdBase = ""
    if secondBase != "":
        score += 1
    if firstBase != "":
        thirdBase = firstBase
        firstBase = ""
    secondBase = lineup[currentBatter]

def doTriple():
    global thirdBase, secondBase, firstBase, score
    if thirdBase != "":
        score += 1
        thirdBase = ""
    if secondBase != "":
        score +=1
        secondBase = ""
    if firstBase != "":
        score +=1
        firstBase = ""
    thirdBase = lineup[currentBatter]

def doHomeRun():
    global thirdBase, secondBase, firstBase, score
    if thirdBase != "":
        score += 1
        thirdBase = ""
    if secondBase != "":
        score += 1
        secondBase = ""
    if firstBase != "":
        score += 1
        firstBase = ""
    score +=1

def doOut():
    global outs, thirdBase, secondBase, firstBase, inning
    outs += 1
    if outs == 3:
        thirdBase = ""
        secondBase = ""
        firstBase = ""
        inning += 1
        outs = 0

def atBat():
    global currentBatter
    printInfo()
    result = input("What did the batter do?").lower()
    if result == "s":
        doSingle()
    elif result == "d":
        doDouble()
    elif result == "t":
        doTriple()
    elif result == "hr":
        doHomeRun()
    else:
        doOut()
    currentBatter += 1


atBat()
atBat()
atBat()
printInfo()
