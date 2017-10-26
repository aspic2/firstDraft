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

    def __init__(self):
        self.length = len(self)
        self.positions = ["QB", "RB", "TE", "K", "DEF", "WR"]

    def fill_list(self):
        queries = [PlayerRepo.defense_query, PlayerRepo.kickers_query, PlayerRepo.offense_query]
        """Populate list and put players in order by points"""
        conn = sqlite3.connect('football.db')
        c = conn.cursor()
        for q in queries:
            player_data = c.execute(q).fetchall()
            for stat in player_data:
                self.append(Player(stat))
        self.sort(key=lambda x: x.points, reverse=True)
        return self

    def draft_player(self, player):
        player.get_drafted()

    def return_available_players(self):
        return list(filter(lambda x: x.available, self))

    def filter_players(self, f, list_len=5):
        """Filters player list of length list_len for position f."""
        return list(filter(lambda x: x.position == f, self))[:list_len]

    def standard_deviation(self, p, n=10):
        """Returns standard deviation of points for best n players in position p"""
        p_list = self.filter_players(p, n)
        # TODO: Can you do this with map()?
        return statistics.stdev(x.points for x in p_list)




