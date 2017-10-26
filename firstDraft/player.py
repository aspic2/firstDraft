# store important info on each player. Also add SQL queries to build players


class Player(object):
    """Object initialized with a list of data points from football.db"""

    def __init__(self, data):
        self.name = data[0] + " " + data[1]
        self.position = data[2]
        self.points = data[3]
        self.available = True

    def get_drafted(self):
        if self.available:
            self.available = False
        return self
