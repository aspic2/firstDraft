"""Does PlayerRepo behave as expected?"""

import unittest
from firstDraft import player_repo


class TestPlayerRepo(unittest.TestCase):

    def setUp(self):
        self.repo = player_repo.PlayerRepo()
        self.repo.fill_list()

    def test_fill_list(self):
        self.assertIsNotNone(self.repo)

    def test_draft_player(self):
        p = self.repo[1]
        self.repo.draft_player(p)
        self.assertEqual(p.available, False)


if __name__ == '__main__':
    unittest.main()
