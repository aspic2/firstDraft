"""Does PlayerRepo behave as expected?"""

import unittest
from firstDraft import player_repo


class TestPlayerRepo(unittest.TestCase):

    def setUp(self):
        self.repo = player_repo.PlayerRepo()
        self.repo.fill_list()
        self.repo[5].available = False

    def test_fill_list(self):
        self.assertIsNotNone(self.repo)

    def test_draft_player(self):
        p = self.repo[1]
        self.repo.draft_player(p)
        self.assertEqual(p.available, False)

    def test_filter_available_players(self):
        available_players = self.repo.filter_available_players()
        no_unavailable_players = None
        for x in available_players:
            if not x.available:
                no_unavailable_players = False
                break
            no_unavailable_players = True
        self.assertTrue(no_unavailable_players)





if __name__ == '__main__':
    unittest.main()
