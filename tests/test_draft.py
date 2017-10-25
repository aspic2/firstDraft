
import unittest
from firstDraft.draft import Draft
from firstDraft.team import Team


class TestDraft(unittest.TestCase):

    def test_teams(self):
        self.draft.teams = Draft(Team("Alpha"), Team("Gold"))
        self.assertTrue(self.draft.teams == 2)

