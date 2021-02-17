from Team import Team
from Player import Player

class Mets(Team):
  def __init__(self):
    player1 = Player("Nimo", .260)
    player2 = Player("McNeil", .305)
    player3 = Player("Lindor", .315)
    player4 = Player("Conforto", .333)
    player5 = Player("Alonso", .240)
    player6 = Player("Smith", .283)
    player7 = Player("Davis", .270)
    player8 = Player("McCann", .275)
    player9 = Player("deGrom", .188)
    super().__init__("Mets", player1, player2, player3, player4, player5, player6, player7, player8, player9)