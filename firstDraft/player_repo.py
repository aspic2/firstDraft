# gather and store pool of players to choose from here

from firstDraft.player import Player
import random


class PlayerRepo(list):

    def __init__(self):
        self.length = len(self)
        self.positions = ["QB", "RB", "TE", "K", "DEF", "WR"]

    def fill_list(self):
        """Populate list and put players in order by points"""
        for num in range(45):
            # TODO: fix this, as it is only filler for tests
            self.append(Player((num, random.choice(self.positions), random.randrange(0, 300))))
        self.sort(key=lambda x: x.points, reverse=True)
        return self

    def draft_player(self, player):
        player.get_drafted()

    def return_available_players(self):
        return filter(lambda x: x.available, self)

    def filter_players(self, f):
        """Filters player list for a specific position."""
        return filter(lambda x: x.position == f, self)



