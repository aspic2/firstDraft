import unittest
from firstDraft.main import run_draft
from firstDraft.draft import Draft


class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertIsInstance(run_draft(), Draft)
