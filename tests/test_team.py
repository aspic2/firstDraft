# create team with quotas for each position and drafting ability

import unittest
from unittest.mock import Mock
from firstDraft.team import Team
from firstDraft.player import Player
from firstDraft.player_repo import PlayerRepo


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team(["Owner", ])
        self.invalid_team_data = [72, ]
        self.invalid_team_data_2 = ["correct name", "2eise8"]
        self.positions = None
        # self.players_list = PlayerRepo([Player(["Player", "1", "QB", 303]), Player(["Player", "2", "RB", 48]),
        #                                Player(["Player", "3", "RB", 120]), Player(["Player", "4", "WR", 237])])
        self.players_list = PlayerRepo().fill_list()

    def test_check_quotas(self):
        # make sure you have x number of players for each position.
        self.team.append(self.players_list[0])
        positions = ["RB", "QB", "DEF"]
        under_quota = self.team.check_quota()
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
        self.assertFalse(self.team.turn)

    def test_view_options(self):
        # TODO: finish revising this in team.py
        options = self.players_list
        results = self.team.view_options(options)
        self.assertIsNotNone(results)

    def test_remove_player(self):
        r = ("Cam Newton", "QB")
        p = self.players_list
        self.team.remove_player(r, p)
        self.assertNotIn(r, self.players_list.return_available_players())

    def test_take_turn_auto(self):
        old_length = len(self.team)
        self.team.take_turn(self.players_list)
        self.assertTrue(len(self.team) == old_length + 1)

    def test_take_turn_manual(self):
        team = Team("Manual", False)
        old_length = len(team)
        team.take_turn(self.players_list)
        self.assertTrue(len(team) == old_length + 1)

    def test_auto_strategy(self):
        old_length = len(self.team)
        pr = PlayerRepo().fill_list().sort_repo()
        strat = "sd"
        new_length = len(self.team.auto_strategy(pr.return_available_players(), strat))
        self.assertTrue(new_length == old_length + 1)
        #self.assertIn(strat, self.team.strategies)

    def test_prompt(self):
        self.assertIsNotNone(self.team.prompt("sd"))



