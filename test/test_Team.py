from unittest import TestCase

from src.Player import Player
from src.Team import Team


def player1():
    return Player("a", .100)


def player2():
    return Player("b", .200)


def player3():
    return Player("c", .300)


def player4():
    return Player("d", .100)


def player5():
    return Player("e", .200)


def player6():
    return Player("f", .300)


def player7():
    return Player("g", .100)


def player8():
    return Player("h", .200)


def player9():
    return Player("i", .300)


class TestTeam(TestCase):
    @staticmethod
    def createTeam():
        return Team("Mets", player1(), player2(), player3(), player4(), player5(), player6(), player7(), player8(),
                    player9())

    def setUp(self):
        self.team = self.createTeam()

    def test_lineup_has_all_nine_players(self):
        assert self.team.lineup == [player1(), player2(), player3(), player4(), player5(), player6(), player7(),
                                    player8(), player9()]

    def test_team_starts_with_score_0(self):
        assert self.team.score == 0

    def test_team_starts_at_first_batter_position_0(self):
        assert self.team.currentBatter == 0

    def test_getCurrentBatterName_gives_name_of_batter_in_linup(self):
        assert self.team.getCurrentBatterName() == player1().name
        self.team.currentBatter = 1
        assert self.team.getCurrentBatterName() == player2().name

    def getCurrentBatterHitChance_gives_average_of_batter_in_lineup(self):
        assert self.team.getCurrentBatterHitChance() == player1().hitChance
        self.team.currentBatter = 1
        assert self.team.getCurrentBatterHitChance() == player2().hitChance
