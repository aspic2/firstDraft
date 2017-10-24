# I guess this checks that all attributes are present


import unittest


from firstDraft.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_data = ["test player", "RB"]

    def test_init(self):
        player = Player(self.player_data)
        self.assertEqual(player.name, self.player_data[0])
        self.assertEqual(player.position, self.player_data[1])
