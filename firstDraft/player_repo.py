# gather and store pool of players to choose from here

from firstDraft.player import Player


class PlayerRepo(list):

    def __init__(self):
        self.length = len(self)

    def fill_list(self):
        for num in range(45):
            # TODO: fix this, as it is only filler for tests
            self.append(Player((num, "WR")))
        return self

    def draft_player(self, player):
        player.get_drafted()

    def filter_available_players(self):
        return filter(lambda x: x.available, self)


