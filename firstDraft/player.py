# store important info on each player. Also add SQL queries to build players


class Player(object):

    def __init__(self, data):
        self.name = data[0]
        self.available = True

    def get_drafted(self):
        if self.available:
            self.available = False
        return self
