from Player import Player
from Mets import Mets
from Game import Game

ourTeam = Mets()
game = Game(ourTeam)
print(ourTeam.lineup)
print(game.ourTeam.name, "- inning", game.inning, "of", game.totalInnings)

def printInfo():
    #Because no variables are being re/assigned a value in this function, the Python interpretor assumes global by default
    print("----------------------------------------------------------")
    if game.firstBase != "":
        print(game.firstBase, "is on first")
    else:
        print("There is no one on first")
    if game.secondBase != "":
        print(game.secondBase, "is on second")
    else:
        print("There is no one on second")
    if game.thirdBase != "":
        print(game.thirdBase, "is on third")
    else:
        print("There is no one on third")
    print("Our score is: " + str(ourTeam.score) +" and the opponent's score is "+ str(game.opponentScore))
    print("There are", game.outs, "outs")
    print("The current batter is", ourTeam.getCurrentBatterName(), "and his batting average is", ourTeam.getCurrentBatterHitChance())
    print("It is currently the", game.inning, "inning")


while game.inning <= game.totalInnings or game.opponentScore == ourTeam.score:
    game.atBat()
    #printInfo()

if ourTeam.score > game.opponentScore:
    print("Our team won "+str(ourTeam.score)+" to "+str(game.opponentScore))
else:
    print("Our team lost "+str(ourTeam.score)+" to "+str(game.opponentScore))


