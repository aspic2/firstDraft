
import unittest
from unittest.mock import Mock
from firstDraft.draft import Draft
from firstDraft.team import Team


class TestDraft(unittest.TestCase):

    def setUp(self):
        # fix Mock to have len() value
        self.draft = Draft([Team("Alpha"), Team("Gold")])

    def test_teams(self):
        self.assertTrue(len(self.draft.teams) == 2)

    def test_selection_round(self):
        starting_no_of_players = len(self.draft.teams[0])
        # test that each team gets to pick a player during a round.
        # test that invalid selections are handled properly and team picks again
        self.draft.selection_round()
        self.assertTrue(len(self.draft.teams[0])) == starting_no_of_players + 1


