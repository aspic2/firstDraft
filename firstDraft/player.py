

class Player(object):
    """Simple object initialized with a list of data points from football.db
    Players "exist()" and get_drafted(), meaning they become unavailable for
    future drafts.
    """

    def __init__(self, data):
        self.name = data[0] + " " + data[1]
        self.position = data[2]
        self.points = data[3]
        self.available = True

    def get_drafted(self):
        if self.available:
            self.available = False
        return self
