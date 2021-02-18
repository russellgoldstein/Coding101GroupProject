from team import Team
from player import Player

class Mets(Team):
  def __init__(self):
    player1 = Player(.260, "Nimmo", "Left")
    player2 = Player(.305, "McNeil", "Left")
    player3 = Player(.315, "Lindor", "Switch")
    player4 = Player(.333, "Conforto", "Left")
    player5 = Player(.240, "Alonso", "Right")
    player6 = Player(.283, "Smith", "Left")
    player7 = Player(.270, "Davis", "Right")
    player8 = Player(.275, "McCann", "Right")
    player9 = Player(.188, "deGrom", "Left")
    super().__init__("Mets", [player1, player2, player3, player4, player5, player6, player7, player8, player9])