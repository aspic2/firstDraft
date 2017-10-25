
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

    def test_round_of_drafts(self):
        starting_no_of_players = len(self.draft.teams[0])
        # test that each team gets to pick a player during a round.
        # test that invalid selections are handled properly and team picks again
        self.draft.round_of_drafts()
        self.assertTrue(len(self.draft.teams[0])) == starting_no_of_players + 1
        # check that second team also had a draft
        self.assertTrue(len(self.draft.teams[1])) == starting_no_of_players + 1

    def test_start(self):
        self.draft.start()
        self.assertEqual(len(self.draft.teams[0]), len(self.draft.teams[1]))
        # TODO: set up Draft() to complete a pre-determined number of rounds
        self.assertEqual(self.draft.number_of_rounds, len(self.draft.teams[-1]))


