# each GM builds a Team() to gain them the most points possible this season


class Team(list):

    quota = {"QB": 1,
             "RB": 2,
             "WR": 2,
             "TE": 1,
             "K": 1,
             "DEF": 1}

    def __init__(self, data):
        self.owner = data[0]
        
    def check_quota(self, positions):
        quota_not_met = []
        for pos in positions:
            num = self.count(lambda player: player.position==pos)
            if num < Team.quota[pos]:
                quota_not_met.append(pos)
        return quota_not_met
        
        

