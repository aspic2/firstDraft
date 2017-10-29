# gather and store pool of players to choose from here

from firstDraft.player import Player
import random
import statistics
import sqlite3


class PlayerRepo(list):
    database = "football.db"
    defense_query = '''SELECT TeamCity, TeamName, Position, Fantasy_Points \
    FROM Defense WHERE Season = 2015
    '''
    kickers_query = '''SELECT FirstName, LastName, Position, \
    Fantasy_Points FROM Kickers WHERE Season = 2015
    '''
    offense_query = '''SELECT FirstName, LastName, Position, \
    Fantasy_Points FROM Offense WHERE Season = 2015
    '''

    def __init__(self, init_list=[]):
        super().__init__(init_list)
        self.length = len(self)
        self.positions = ["QB", "RB", "TE", "K", "DEF", "WR"]
        self.player_dict = {}

    def fill_list(self):
        """Populate PlayerRepo() and put players in order by points"""
        queries = [PlayerRepo.defense_query, PlayerRepo.kickers_query, PlayerRepo.offense_query]
        conn = sqlite3.connect('football.db')
        c = conn.cursor()
        for q in queries:
            player_data = c.execute(q).fetchall()
            for stat in player_data:
                self.append(Player(stat))
        for p in self:
            self.player_dict[(p.name, p.position)] = p
        return self

    def sort_repo(self):
        self.sort(key=lambda x: x.points, reverse=True)
        return self

    def draft_player(self, player):
        player.get_drafted()

    def return_available_players(self):
        return PlayerRepo(filter(lambda x: x.available, self))

    def filter_players(self, f, list_len=5):
        """Filters player list of length list_len for position f."""
        return list(filter(lambda x: x.position == f, self))[:list_len]

    def standard_deviation(self, position, n=10):
        """Returns standard deviation of points for best n players in position p"""
        p_list = self.filter_players(position, n)
        # TODO: Can you do this with map()?
        # return statistics.stdev(map(lambda x: x.points, p_list))
        # TODO: A: Yes, but it is not as clear as the list comprehension
        return statistics.stdev(x.points for x in p_list)

    def return_player(self, name_and_position):
        if name_and_position in self.player_dict:
            return self.player_dict[name_and_position]
        else:
            print(name_and_position[0] + " not found")
            return None





