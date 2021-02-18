import random
from mets import Mets
from game import Game
ourTeam = Mets()
ourTeam.printTeamStats()

ourGame = Game(ourTeam)

while ourGame.inning <= ourGame.totalInnings or ourGame.opponentScore == ourGame.ourTeam.score:
    ourGame.atBat()

if ourGame.ourTeam.score > ourGame.opponentScore:
    print("Our team won "+str(ourGame.ourTeam.score)+" to "+str(ourGame.opponentScore))
else:
    print("Our team lost "+str(ourGame.ourTeam.score)+" to "+str(ourGame.opponentScore))