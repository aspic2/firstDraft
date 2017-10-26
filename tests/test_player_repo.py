"""Does PlayerRepo behave as expected?"""

import unittest
import random
from firstDraft import player_repo


class TestPlayerRepo(unittest.TestCase):

    def setUp(self):
        self.repo = player_repo.PlayerRepo()
        self.repo.fill_list()
        self.repo[5].available = False

    def test_fill_list(self):
        """Confirm that list is populated and in order"""
        self.assertIsNotNone(self.repo)
        self.assertTrue(self.repo[3].points > self.repo[4].points)
        self.assertTrue(self.repo[4].points > self.repo[5].points)

    def test_draft_player(self):
        p = self.repo[1]
        self.repo.draft_player(p)
        self.assertEqual(p.available, False)

    def test_return_available_players(self):
        available_players = self.repo.return_available_players()
        no_unavailable_players = None
        for x in available_players:
            if not x.available:
                no_unavailable_players = False
                break
            no_unavailable_players = True
        self.assertTrue(no_unavailable_players)

    def test_filter_players(self):
        """Method returns top 5 players given a specific filter."""
        # This random method may cause a false negative if sample is too small!
        f = random.choice(self.repo.positions)
        length = 6
        filtered_list = self.repo.filter_players(f, length)
        self.assertTrue(len(filtered_list) == length)
        filter_works = None
        for player in filtered_list:
            if player.position != f:
                filter_works = False
                break
            filter_works = True
        self.assertTrue(filter_works)
        # confirm that list is still in order
        self.assertTrue(filtered_list[0].points > filtered_list[-1].points)
        self.assertTrue(filtered_list[3].points > filtered_list[4].points)

    def test_standard_deviation(self):
        p = random.choice(self.repo.positions)
        sd = self.repo.standard_deviation(p, 25)
        self.assertIsNotNone(sd)









if __name__ == '__main__':
    unittest.main()
