#Main module for fantastic, the fantasy football virtual GM

"""Build your algorithm to rank players based on the following scoring system
and team allowance:

DEFAULT TEAM SIZE: 15 players
Player Mins:
QB = 1
RB = 2
WR = 2
TE = 1
K = 1
DEF = 1
= 8
+1 additional flex player
= 9
+6 bench players
= 15

DEFAULT NFL-MANAGED SCORING SETTINGS:
OFFENSE

Passing Yards: 1 point per 25 yards passing
Passing Touchdowns: 4 points
Interceptions: -2 points
Rushing Yards: 1 point per 10 yards
Rushing Touchdowns: 6 points
Receiving Yards: 1 point per 10 yards
Receiving Touchdowns: 6 points
Fumble Recovered for a Touchdown: 6 points
2-Point Conversions: 2 points
Fumbles Lost: -2 points


KICKING

PAT Made: 1 point
FG Made (0-49 yards): 3 points
FG Made (50+ yards): 5 points


DEFENSE TEAM

Sacks: 1 point
Interceptions: 2 points
Fumbles Recovered: 2 points
Safeties: 2 points
Defensive Touchdowns: 6 points
Kick and Punt Return Touchdowns: 6 points
Points Allowed (0): 10 points
Points Allowed (1-6): 7 points
Points Allowed (7-13): 4 points
Points Allowed (14-20): 1 points
Points Allowed (21-27): 0 points
Points Allowed (28-34): -1 points
Points Allowed (35+): -4 points


GENERAL SCORING SETTINGS

Use Fractional Points: Yes
Use Negative Points: Yes

"""

import sqlite3
from os import getcwd

database = "football.db"
defense_query = '''SELECT Season, Position, TeamCity, TeamName, Fantasy_Points \
FROM Defense WHERE Season = 2015
'''
kickers_query = '''SELECT Season, Position, FirstName, LastName, Team, \
Fantasy_Points FROM Kickers WHERE Season = 2015
'''
offense_query = '''SELECT Season, Position, FirstName, LastName, Team, \
Fantasy_Points FROM Offense WHERE Season = 2015
'''

class Team(object):

    def __init__(self, owner):
        self.owner = owner
        self.defs = []
        self.ks = []
        self.rbs = []
        self.qbs = []
        self.tes = []
        self.wrs = []


class Player(object):
    """Assemble players with different stats and a full rating, then compare
    player to his position-mates
    """
    def __init__(self, position, name, nfl_team, points):
        self.position = position
        self.name = name
        self.nfl_team = nfl_team
        self.point = points

class Data(object):

    def get_data(query):
        conn = sqlite3.connect('football.db')
        c = conn.cursor()
        player_data = c.execute(query).fetchall()
        return player_data

    def build_players(query):
        players = []
        data = Data.get_data(query)
        for stat in data:
            # switch for the 3 different score sysems
            # names are tuples in format (firstName, lastName)
            if query == offense_query:
                players.append(Player(stat[1], (stat[2], stat[3]), stat[4], stat[5]))
            elif query == defense_query:
                players.append(Player(stat[1], (stat[2], stat[3]), stat[3], stat[4]))
            elif query == kickers_query:
                players.append(Player(stat[1], (stat[2], stat[3]), stat[4], stat[5]))
            else:
                print("Was unable to create players using data.")
                return [-1]
        for player in players:
            print(player.name)
        return players


def main():
    defenses = Data.build_players(defense_query)
    offenses = Data.build_players(offense_query)
    kickers = Data.build_players(kickers_query)


if __name__ == '__main__':
    main()
