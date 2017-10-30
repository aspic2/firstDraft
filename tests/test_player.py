# I guess this checks that all attributes are present


import unittest


from firstDraft.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_data = ["test", "player", "RB", 100]

    def test_init(self):
        player = Player(self.player_data)
        self.assertEqual(player.name, self.player_data[0] + " " + self.player_data[1])
        self.assertEqual(player.position, self.player_data[2])
        self.assertIsNotNone(player.points)

    def test_get_drafted(self):
        player = Player(self.player_data)
        player.get_drafted()
        self.assertFalse(player.available)


if __name__ == '__main__':
    unittest.main()