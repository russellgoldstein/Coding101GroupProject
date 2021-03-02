from unittest import TestCase

from src.Game import Game
from test_Team import TestTeam

class TestGame(TestCase):
    def setUp(self):
        self.team = TestTeam.createTeam()
        self.game = Game(self.team)

    def test_game_starting_values(self):
        assert self.game.inning == 1
        assert self.game.outs == 0
        assert self.game.firstBase == ""
        assert self.game.secondBase == ""
        assert self.game.thirdBase == ""
        assert self.game.totalInnings == 9
        assert self.game.opponentScore == 0

    def bases_empty(self):
        assert self.game.firstBase == ""
        assert self.game.secondBase == ""
        assert self.game.thirdBase == ""

    def test_doSingle_with_empty_bases_does_not_change_score_only_runner_on_first(self):
        self.bases_empty()
        self.game.ourTeam.score = 0
        self.game.ourTeam.currentBatter = 0
        self.game.doSingle()
        assert self.game.ourTeam.score == 0
        assert self.game.firstBase == self.game.ourTeam.lineup[0].name
        assert self.game.secondBase == ""
        assert self.game.thirdBase == ""

    def test_doSingle_with_man_on_first_does_not_change_score_runner_on_first_and_second(self):
        self.bases_empty()
        self.game.firstBase = "Bob"
        self.game.ourTeam.score = 0
        self.game.ourTeam.currentBatter = 0
        self.game.doSingle()
        assert self.game.ourTeam.score == 0
        assert self.game.firstBase == self.game.ourTeam.lineup[0].name
        assert self.game.secondBase == "Bob"
        assert self.game.thirdBase == ""

    def test_doSingle_with_man_on_first_and_second_does_not_change_score_runner_on_first_second_and_thrid(self):
        self.bases_empty()
        self.game.firstBase = "Bob"
        self.game.secondBase = "Joe"
        self.game.ourTeam.score = 0
        self.game.ourTeam.currentBatter = 0
        self.game.doSingle()
        assert self.game.ourTeam.score == 0
        assert self.game.firstBase == self.game.ourTeam.lineup[0].name
        assert self.game.secondBase == "Bob"
        assert self.game.thirdBase == "Joe"

    def test_doSingle_with_bases_loaded_does_change_score_bases_still_loaded(self):
        self.bases_empty()
        self.game.firstBase = "Bob"
        self.game.secondBase = "Joe"
        self.game.thirdBase = "Brian"
        self.game.ourTeam.score = 0
        self.game.ourTeam.currentBatter = 0
        self.game.doSingle()
        assert self.game.ourTeam.score == 1
        assert self.game.firstBase == self.game.ourTeam.lineup[0].name
        assert self.game.secondBase == "Bob"
        assert self.game.thirdBase == "Joe"