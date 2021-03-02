from unittest import TestCase

from src.Player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Bob", .250)

    def test_player_repr_is_their_name(self):
        assert self.player.__repr__() == "Bob"

    def test_players_with_same_name_but_diff_ave_are_not_equal(self):
        assert Player("Bob", .200) != Player("Bob", .201)

    def test_players_with_same_ave_but_diff_name_are_not_equal(self):
        assert Player("Bob", .200) != Player("Bobby", .200)

    def test_players_with_same_name_and_same_ave_are_equal(self):
        assert Player("Bob", .200) == Player("Bob", .200)