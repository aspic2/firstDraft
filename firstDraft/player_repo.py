# gather and store pool of players to choose from here

from firstDraft.player import Player
import random
import statistics
import sqlite3


class PlayerRepo(list):
    """List subclass with additional methods to return useful data about players.
    Class contains attributes to query the database and fill the repo properly.
    """
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
        """Initialize with standard list() init."""
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
        return self

    def fill_dict(self):
        """This function _must_ be called to use Team.find() and 
        PlayerRepo.return_player() methods. Seemed like it would be better than
        calling a linear search each time.
        """
        for p in self:
            self.player_dict[(p.name, p.position)] = p
        return self

    def sort_repo(self):
        """Puts repo in descending order by points. (Highest point player first.)
        Only needs to be called once per repo
        """
        self.sort(key=lambda x: x.points, reverse=True)
        return self

    def draft_player(self, player):
        player.get_drafted()

    def return_available_players(self):
        """Returns new repo of only players that are still available
        (i.e. not drafted or removed)
        """
        return PlayerRepo(filter(lambda x: x.available, self)).fill_dict()

    def filter_by_position(self, f, list_len=10):
        """Filters player list for position f and returns new list truncated to list_len."""
        return list(filter(lambda x: x.position == f, self))[:list_len]

    def standard_deviation(self, position, n=10):
        """Returns standard deviation of points for best n players in position p"""
        p_list = self.filter_by_position(position, n)
        # TODO: Can you do this with map()?
        # return statistics.stdev(map(lambda x: x.points, p_list))
        # TODO: A: Yes, but it is not as clear as the list comprehension
        return statistics.stdev(x.points for x in p_list)

    def return_player(self, name_and_position):
        """Received tuple("Player Name", "Position") from Team.find_player().
        Returns player if exists in player_dict. Returns None otherwise"""
        if name_and_position in self.player_dict:
            found = self.player_dict[name_and_position]
            print(found.name + " found")
            return found
        else:
            print(name_and_position[0] + ", " + name_and_position[1] + " not found")
            return None





