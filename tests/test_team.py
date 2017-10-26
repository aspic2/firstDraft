# create team with quotas for each position and drafting ability

import unittest
from firstDraft.team import Team
from firstDraft.player import Player


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team(["Owner", ])
        self.invalid_team_data = [72, ]
        self.invalid_team_data_2 = ["correct name", "2eise8"]
        self.positions = None
        self.players_list = [Player(["Player1", "QB"]), Player(["Player2", "RB"])]

    def test_check_quotas(self):
        # make sure you have x number of players for each position.
        self.team.append(self.players_list[0])
        positions = ["RB", "QB", "DEF"]
        under_quota = self.team.check_quota(positions)
        self.assertIsNotNone(under_quota)
        self.assertNotEqual(under_quota[0], self.players_list[0])

    def test_draft_player(self):
        # make sure player appears on your team and is unavailable to others
        p = self.players_list[0]
        self.team.draft_player(p)
        # test that player is on team
        self.assertIn(p, self.team)
        # test that player is unavailable from the player repo
        # TODO: should this be in test_player?
        self.assertFalse(p.available)

    def test_view_options(self):
        #TODO: finish revising this in team.py
        options = []
        results = self.team.view_options(options)
        self.assertIsNotNone(results)


